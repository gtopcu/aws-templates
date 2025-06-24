import json
import os
from abc import ABC
from collections import defaultdict
from collections.abc import Iterable
from datetime import date
from enum import Enum
from functools import lru_cache
from typing import Union, List, Dict, Any, Generator
from aws_lambda_powertools import Logger
import boto3
from botocore.exceptions import ClientError

from boto3.dynamodb.conditions import Key
from mypy_boto3_dynamodb.service_resource import Table

from secr.domain.model.conversion_factor import (
    ConversionFactor,
    DefaultConversionFactor,
    RangedConversionFactor,
)
from secr.repository.conversion_factor_repository import IConversionFactorRepository
from secr.repository.dynamodb.dd_client import get_ddb_resource
import orjson

ENV_DATA_TABLE = "GLOBAL_CONSTANTS_DATA_TABLE"
DATA_BUCKET_NAME_ENV = "DATA_BUCKET_NAME"

PARTITION_KEY = "PK"
SORT_KEY = "SK"
PARTITION_KEY_VALUE = "ConversionFactor"

logger = Logger()


class DDConversionFactorRepository(IConversionFactorRepository, ABC):
    __table: Table

    def __init__(self):
        ddb = get_ddb_resource()
        self.__table = ddb.Table(os.getenv(ENV_DATA_TABLE))
        self.s3 = boto3.client("s3")
        self.S3_BUCKET = os.getenv(DATA_BUCKET_NAME_ENV)
        self.S3_CACHE_KEY = "conversion_factors.json"

    def save_factors(self, factors: Iterable[ConversionFactor]) -> None:
        logger.info("Saving conversion factors and clearing cache...")

        # Step 1: Clear the existing cache in S3
        self._clear_s3_cache()

        # Step 2: Save the new factors in DynamoDB
        try:
            with self.__table.batch_writer() as batch_writer:
                for cf in factors:
                    batch_writer.put_item(Item=_factor_to_dict(cf))
        except Exception as e:
            logger.exception(e)
            raise
        else:
            logger.info("Saved conversion factors to DynamoDB.")

        # Step 3: Recreate the cache with the new data
        self._recreate_cache()

    def get_factors(self) -> Iterable[ConversionFactor]:
        """Fetch conversion factors from S3 cache if available, otherwise from DynamoDB."""
        logger.info("Getting conversion factors...")

        # Step 1: Try to fetch from S3 cache
        try:
            s3_data = self.s3.get_object(Bucket=self.S3_BUCKET, Key=self.S3_CACHE_KEY)
            body = s3_data["Body"].read()  # Read S3 Data

            cached_data = orjson.loads(body)  # Fastest JSON Parsing
            print(type(cached_data))
            if not isinstance(cached_data, list):
                raise ValueError(
                    "Unexpected JSON format: Expected a list"
                )  # Fail fast if not list

            for item in cached_data:
                yield _factor_from_dict(item)  # Convert & Yield Factors

            return
        except Exception:
            logger.exception(
                "Error fetching from S3 cache, proceeding to query DynamoDB"
            )

        try:
            kwargs = {}
            all_factors = []  # Store all the factors to cache later
            while True:
                response = self.__table.query(
                    KeyConditionExpression=Key(PARTITION_KEY).eq(PARTITION_KEY_VALUE),
                    **kwargs,
                )
                logger.info(f"Fetched {response['Count']} items from DynamoDB.")

                for item in response["Items"]:
                    cf = _factor_from_dict(item)
                    all_factors.append(cf)
                    yield cf

                if "LastEvaluatedKey" in response:
                    logger.info(
                        f"Fetching more items... LastEvaluatedKey: {response['LastEvaluatedKey']}"
                    )
                    kwargs.update({"ExclusiveStartKey": response["LastEvaluatedKey"]})
                else:
                    logger.debug("No more items to fetch.")
                    break
        except Exception:
            logger.exception("Error querying DynamoDB")
            raise
        else:
            logger.info("Fetched conversion factors successfully from DynamoDB.")

    def _save_to_s3(self) -> None:
        """Save the fetched conversion factors to S3 as a cache."""

        try:
            all_factors = self.get_factors()
            # Check if data contains dicts instead of ConversionFactor instances
            serialized_data = json.dumps(
                [
                    cf.model_dump(mode="json", exclude_none=True)
                    if isinstance(cf, ConversionFactor)
                    else cf
                    for cf in all_factors
                ]
            )
            self.s3.put_object(
                Bucket=self.S3_BUCKET,
                Key=self.S3_CACHE_KEY,
                Body=serialized_data,  # Use the custom encoder
                ContentType="application/json",
            )
            logger.info(f"Saved conversion factors to S3 cache at {self.S3_CACHE_KEY}.")
        except ClientError as e:
            error_code = e.response["Error"]["Code"]
            if error_code == "404":
                logger.info("S3 cache file does not exist. Querying DynamoDB...")
            else:
                # Log other ClientErrors that are not 404
                logger.error(f"Unexpected ClientError: {e}")
                raise
        except Exception as e:
            logger.exception(f"Failed to save data to S3: {e}")
            raise

    def _clear_s3_cache(self) -> None:
        """Clear the cache in S3 by deleting the cache file."""
        try:
            self.s3.delete_object(Bucket=self.S3_BUCKET, Key=self.S3_CACHE_KEY)
            logger.info(f"Cleared S3 cache: {self.S3_CACHE_KEY}.")
        except self.s3.exceptions.NoSuchKey:
            logger.info("No cache file to delete in S3.")
        except Exception as e:
            logger.exception(f"Failed to clear cache in S3: {e}")
            raise

    def _recreate_cache(self) -> None:
        """Recreate the cache in S3 after saving new factors to DynamoDB."""
        logger.info("Recreating S3 cache with the newly saved factors.")
        self._save_to_s3()

    def delete_all_factors(self) -> None:
        _keys = self.__table.query(
            KeyConditionExpression=Key(PARTITION_KEY).eq(PARTITION_KEY_VALUE),
            ProjectionExpression=",".join([PARTITION_KEY, SORT_KEY]),
        )["Items"]
        logger.info("Deleting all conversion factors!")
        try:
            with self.__table.batch_writer() as batch_writer:
                for _key in _keys:
                    batch_writer.delete_item(Key=_key)
        except Exception as e:
            logger.exception(e)
            raise
        else:
            logger.info("Successfully deleted all conversion factors.")

    def get_permutations_by_category(self, ignore_keys: list[str] | None = None) -> str:
        if ignore_keys is None:
            ignore_keys = []

        conversion_factors = get_conversion_factor_repository().get_factors()
        category_permutations = defaultdict(
            lambda: defaultdict(lambda: defaultdict(list))
        )

        for cf in conversion_factors:
            category = cf.category
            attributes = cf.__dict__

            if "category" not in ignore_keys:
                ignore_keys.append(
                    "category"
                )  # Ensure category key is ignored in nested levels

            for key, value in attributes.items():
                if key not in ignore_keys and value is not None:
                    if isinstance(value, Enum):
                        value = value.name  # Convert enum to string representation

                    if value not in category_permutations[category][key]:
                        category_permutations[category][key][value] = defaultdict(list)

                    for sub_key, sub_value in attributes.items():
                        if (
                            sub_key not in ignore_keys
                            and sub_value is not None
                            and sub_key != key
                        ):
                            if isinstance(sub_value, Enum):
                                sub_value = (
                                    sub_value.name
                                )  # Convert enum to string representation

                            if (
                                sub_value
                                not in category_permutations[category][key][value][
                                    sub_key
                                ]
                            ):
                                category_permutations[category][key][value][
                                    sub_key
                                ].append(sub_value)

        return json.dumps(
            category_permutations,
            default=lambda x: list(x) if isinstance(x, set) else x,
        )

    def get_conversion_factors_by_sic(
        self, sic_codes: List[str]
    ) -> Dict[str, Dict[str, ConversionFactor]]:
        """
        Retrieve the latest conversion factor for each SIC code and country.
        """
        results = {}
        for sic_code in sic_codes:
            factors_by_country = {}  # To store latest factor per country for current SIC code

            # Query DynamoDB with begins_with filter on SORT_KEY for each SIC code
            try:
                response = self.__table.query(
                    KeyConditionExpression=Key(PARTITION_KEY).eq(PARTITION_KEY_VALUE)
                    & Key(SORT_KEY).begins_with(f"SCOPE_3_PURCHASE:GBP:{sic_code}:")
                )
                for item in response.get("Items", []):
                    cf = _factor_from_dict(item)
                    country_code = cf.country_code

                    existing_cf = factors_by_country.get(country_code)

                    if existing_cf:
                        if isinstance(
                            existing_cf, DefaultConversionFactor
                        ) and isinstance(cf, RangedConversionFactor):
                            factors_by_country[country_code] = cf
                        elif isinstance(cf, RangedConversionFactor) and (
                            not isinstance(existing_cf, RangedConversionFactor)
                            or cf.start_date > existing_cf.start_date
                        ):
                            factors_by_country[country_code] = cf
                    else:
                        factors_by_country[country_code] = cf

            except Exception as e:
                logger.exception(
                    f"Error retrieving conversion factors for SIC code {sic_code}: {e}"
                )
                continue

            results[sic_code] = factors_by_country  # Add results for current SIC code

        # Convert dates to strings in results to make JSON serializable
        for sic_code, countries in results.items():
            for country_code, factor in countries.items():
                if isinstance(factor, RangedConversionFactor):
                    if isinstance(factor.start_date, date):
                        factor.start_date = factor.start_date.isoformat()
                    if isinstance(factor.end_date, date):
                        factor.end_date = factor.end_date.isoformat()

        return results


def _factor_to_dict(cf: ConversionFactor) -> dict:
    cf_dict = cf.model_dump(mode="json", exclude_none=True)
    cf_dict.update(_get_key(cf))

    return cf_dict


def _factor_from_dict(cf_dict: dict) -> ConversionFactor:
    return ConversionFactor.parse_subclass(**cf_dict)


def _get_key(cf: ConversionFactor) -> dict:
    return {
        PARTITION_KEY: PARTITION_KEY_VALUE,
        SORT_KEY: cf.identifier,
    }


@lru_cache
def get_conversion_factor_repository() -> IConversionFactorRepository:
    """
    Always use this to fetch an instance of repository. It is cached.
    """
    return DDConversionFactorRepository()
