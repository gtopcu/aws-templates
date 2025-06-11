
import os
from typing import Iterable
from functools import lru_cache, partial
from datetime import datetime

from aws_lambda_powertools import Logger
import boto3
from boto3.dynamodb.conditions import Key, Attr
from botocore.exceptions import ClientError
from mypy_boto3_dynamodb.service_resource import Table
from mypy_boto3_dynamodb.type_defs import QueryOutputTableTypeDef


ENV_DDB_TABLE = "companies"
PARTITION_KEY = "PK"
SORT_KEY = "SK"

COMPANY_SORT_KEY_PREFIX = "Company"
FACILITY_SORT_KEY_PREFIX = "CompanyFacility:"
USER_SORT_KEY_PREFIX = "CompanyUser:"

logger = Logger()

class Company:
    company_id: str
    company_name: str

class Facility: ...
class User: ...

from enum import StrEnum
class UserRole(StrEnum):
    ADMIN = "Admin"


class DDB_Company():
    __table: Table

    def __init__(self):
        ddb = boto3.resource("dynamodb")
        self.__table = ddb.Table(os.getenv(ENV_DDB_TABLE))

    def create_company(self, company: Company) -> None:
        """
        Creates a new company. Throws an exception if the company already exists
        """
        logger.info(
            f"Creating company. id={company.company_id} name={company.company_name}"
        )
        try:
            self.__table.put_item(
                Item=(_company_to_dict(company)),
                ConditionExpression=f"attribute_not_exists({PARTITION_KEY})",
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                msg = f"Company id={company.company_id} already exists"
                logger.exception(msg)
                raise Exception(msg)
            else:
                logger.exception(e)
                raise
        else:
            logger.info(
                f"Company created. id={company.company_id} name={company.company_name}"
            )

    def update_company(self, company: Company) -> None:
        """
        Updates an existing company. Throws an exception if the company does not exist
        """
        logger.info(f"Updating company with id={company.company_id}")
        try:
            self.__table.put_item(
                Item=(_company_to_dict(company)),
                ConditionExpression=f"attribute_exists({PARTITION_KEY})",
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                msg = f'Company "{company.company_name}" does not exist!'
                logger.exception(msg)
                raise Exception(msg)
            else:
                logger.exception(e)
                raise
        else:
            logger.info(f"Company updated. id={company.company_id}")

    # def get_full_company(
    #     self, company_id: str
    # ) -> tuple[Company, Iterable[Facility], Iterable[User]]:
    #     logger.info(f"Getting full company information for {company_id}.")
    #     start_time = datetime.now()
    #     try:
    #         query_start = datetime.now()
    #         result: QueryOutputTableTypeDef = self.__table.query(
    #             KeyConditionExpression=Key(PARTITION_KEY).eq(company_id)
    #             & Key(SORT_KEY).begins_with(COMPANY_SORT_KEY)
    #         )
    #         query_time = (datetime.now() - query_start).total_seconds()
    #         logger.info(f"DynamoDB query execution time: {query_time} seconds")

    #     except ClientError as e:
    #         logger.exception(e)
    #         raise
    #     else:
    #         logger.info(f"Fetched company. id={company_id}.")

    #         return (
    #             next(
    #                 _company_from_dict(item)
    #                 for item in result["Items"]
    #                 if item.get(SORT_KEY) == COMPANY_SORT_KEY
    #             ),
    #             (
    #                 _facility_from_dict(item)
    #                 for item in result["Items"]
    #                 if item.get(SORT_KEY).startswith(FACILITY_SORT_KEY_PREFIX)
    #             ),
    #             (
    #                 _user_from_dict(item)
    #                 for item in result["Items"]
    #                 if item.get(SORT_KEY).startswith(USER_SORT_KEY_PREFIX)
    #                 and item.get("role") != UserRole.ADMIN
    #             ),
    #         )

    def get_company_by_id_with_children(self, company_id: str) -> tuple[Company, Iterable[Facility], Iterable[User]]:
        start_time = datetime.now()
        logger.info(f"Getting company with id: {company_id}")

        try:
            # query_start = datetime.now()
            result: QueryOutputTableTypeDef = self.__table.query(
                KeyConditionExpression=Key(PARTITION_KEY).eq(company_id)
                                     & Key(SORT_KEY).begins_with(COMPANY_SORT_KEY_PREFIX)
            )
            items = result["Items"]

            company = None
            facilities = []
            users = []

            for item in items:
                sort_key = item.get(SORT_KEY)

                if sort_key == COMPANY_SORT_KEY_PREFIX:
                    company = _company_from_dict(item)
                elif sort_key.startswith(FACILITY_SORT_KEY_PREFIX):
                    facilities.append(_facility_from_dict(item))
                elif (
                    sort_key.startswith(USER_SORT_KEY_PREFIX)
                    and item.get("role") != UserRole.ADMIN
                ):
                    users.append(_user_from_dict(item))

            # Log execution times
            total_processing_time = (datetime.now() - start_time).total_seconds()
            logger.info(f"Total processing time: {total_processing_time} seconds")

        except ClientError as e:
            logger.exception(e)
            raise
        else:
            total_time = (datetime.now() - start_time).total_seconds()
            logger.info(f"Total execution time: {total_time} seconds")
            logger.info(f"Fetched company with id: {company_id}")
            return (company, facilities, users)

    def get_company_by_id(self, company_id: str) -> Company | None:
        logger.info(f"Getting company with id: {company_id}")
        try:
            result = self.__table.get_item(
                Key={
                    PARTITION_KEY: company_id,
                    SORT_KEY: COMPANY_SORT_KEY_PREFIX,
                }
            )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            if result.get("Item") is None:
                return None
            logger.info(f"Fetched company with id: {company_id}")
            return _company_from_dict(result["Item"])

    def get_company_id_by_company_name(self, company_name: str) -> str:
        
        result = self.__table.query(
            KeyConditionExpression=Key("company_name").eq(company_name),
            IndexName="CompanyNameIndex",
            ProjectionExpression=PARTITION_KEY,
            Limit=1,
        )

        if len(result["Items"]) < 1:
            msg = f'Company with name "{company_name}" does not exist!'
            logger.exception(msg)
            raise Exception(msg)
        return result["Items"][0].get(PARTITION_KEY)

    def get_company_id_by_subdomain(self, sub_domain: str) -> str:
        """
        Finds the relevant company id from the DynamoDB database by subdomain.
        """
        result = self.__table.query(
            KeyConditionExpression=Key("sub_domain").eq(sub_domain),
            IndexName="SubdomainIndex",
            ProjectionExpression=PARTITION_KEY,
            Limit=1,
        )

        if len(result["Items"]) < 1:
            msg = f'Company with sub_domain "{sub_domain}" does not exist!'
            logger.exception(msg)
            raise Exception(msg)
        return result["Items"][0].get(PARTITION_KEY)

    def get_companies(self) -> Iterable[Company]:
        logger.info("Getting all companies.")
        try:
            result: QueryOutputTableTypeDef = self.__table.query(
                IndexName="InvertedIndex",
                KeyConditionExpression=Key(SORT_KEY).eq(COMPANY_SORT_KEY_PREFIX),
            )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info("Fetched all companies.")
            return (_company_from_dict(item) for item in result["Items"])

    def deactivate_company(self, company_id: str) -> None:
        """
        Updates the company to not active
        """
        logger.info(f"Attempting to de-activate company. id={company_id}")
        try:
            self.__table.update_item(
                Key={PARTITION_KEY: company_id, SORT_KEY: COMPANY_SORT_KEY_PREFIX},
                UpdateExpression="set IsActive=:r",
                ExpressionAttributeValues={":r": 0},
                ConditionExpression=f"attribute_exists({PARTITION_KEY})",
            )
        except ClientError as e:
            if e.response["Error"]["Code"] == "ConditionalCheckFailedException":
                logger.exception(
                    f'Could not de-activate. Company with id "{company_id}" does not exist!'
                )
            else:
                logger.exception(e)
            raise
        else:
            logger.info(f"Company de-activated. id={company_id}")

    def delete_company(self, company_id: str) -> None:
        """
        Deletes the company permanently
        """
        logger.info(
            f"Attempting to delete company and associated records. id={company_id}"
        )

        _keys = self.__table.query(
            KeyConditionExpression=Key(PARTITION_KEY).eq(company_id),
            ProjectionExpression=",".join([PARTITION_KEY, SORT_KEY]),
        )["Items"]
        try:
            with self.__table.batch_writer() as batch_writer:
                for _key in _keys:
                    batch_writer.delete_item(Key=_key)
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(f"Company permanently deleted. id={company_id}")

    def save_facilities(self, facilities: Iterable[Facility]) -> None:
        logger.info("Saving facilities..")
        facilities_pascal_case = (
            _facility_to_dict(facility) for facility in facilities
        )
        facility_names: list[str] = []
        try:
            with self.__table.batch_writer() as batch_writer:
                for facility in facilities_pascal_case:
                    facility_names.append(facility["facility_name"])
                    batch_writer.put_item(Item=facility)
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(f"Saved facilities {facility_names}.")

    def get_company_facilities(self, company_id: str) -> Iterable[Facility]:
        try:
            result: QueryOutputTableTypeDef = self.__table.query(
                KeyConditionExpression=Key(PARTITION_KEY).eq(company_id)
                & Key(SORT_KEY).begins_with(FACILITY_SORT_KEY_PREFIX)
            )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(f"Fetched facilities for company. id={company_id}")
            return (_facility_from_dict(item) for item in result["Items"])

    def delete_facilities(self, facilities: Iterable[Facility]) -> None:
        logger.info("Deleting facilities.")
        try:
            with self.__table.batch_writer() as batch_writer:
                for facility in facilities:
                    batch_writer.delete_item(
                        Key={
                            PARTITION_KEY: facility.company_id,
                            SORT_KEY: FACILITY_SORT_KEY_PREFIX + facility.facility_id,
                        }
                    )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info("Deleted facilities.")

    def save_users(self, users: Iterable[User]) -> None:
        logger.info("Saving users.")
        try:
            with self.__table.batch_writer() as batch_writer:
                for user in users:
                    batch_writer.put_item(Item=_user_to_dict(user))
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info("Saved users.")

    def get_users(self, company_id: str) -> Iterable[User]:
        logger.info(f"Fetching users for company. id={company_id}")
        try:
            result: QueryOutputTableTypeDef = self.__table.query(
                KeyConditionExpression=Key(PARTITION_KEY).eq(company_id)
                & Key(SORT_KEY).begins_with(USER_SORT_KEY_PREFIX)
            )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(f"Fetched users for company. id={company_id}")
            return (_user_from_dict(item) for item in result["Items"])

    def delete_users(self, users: Iterable[User]) -> None:
        logger.info("Deleting users.")
        try:
            with self.__table.batch_writer() as batch_writer:
                for user in users:
                    batch_writer.delete_item(
                        Key={
                            PARTITION_KEY: user.company_id,
                            SORT_KEY: USER_SORT_KEY_PREFIX + user.email,
                        }
                    )
        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info("Deleted users.")

    def get_companies_for_tasks(self) -> Iterable[Company]:
        logger.info("Getting all companies.")
        try:
            # thirty_days_ago = (datetime.utcnow() - timedelta(days=30)).isoformat() + "Z"

            # x = self.__table
            result: QueryOutputTableTypeDef = self.__table.query(
                IndexName="InvertedIndex",
                KeyConditionExpression=Key(SORT_KEY).eq(COMPANY_SORT_KEY_PREFIX),
                FilterExpression=Attr("company_assignments").exists(),
            )

        except ClientError as e:
            logger.exception(e)
            raise
        else:
            logger.info(
                "Fetched all companies with company assignments that have not been updated in 30 days."
            )
            return (_company_from_dict(item) for item in result["Items"])

    def update_last_updated_in_company_assignment(self, company_id, category):
        try:
            # new_last_updated = datetime.utcnow().isoformat()
            new_last_updated = datetime.utcnow().date().isoformat()
            response = self.__table.get_item(
                Key={
                    PARTITION_KEY: company_id,
                    SORT_KEY: COMPANY_SORT_KEY_PREFIX,
                }
            )
            # Check if the item exists
            if "Item" not in response:
                print("Item not found!")
                exit()

            # Get the companyAssignments list
            # company_assignments = response['Item'].get('companyAssignments', {}).get('L', [])
            company_assignments = response["Item"].get("company_assignments", [])

            # Step 2: Find the index of the 'WASTE' category in the companyAssignments list
            index_to_update = None
            for i, assignment in enumerate(company_assignments):
                if assignment.get("category"):
                    if assignment["category"] == category:
                        index_to_update = i
                        break
                if (
                    "M" in assignment
                    and assignment["M"].get("category", {}).get("S") == category
                ):
                    index_to_update = i
                    break
                else:
                    print("not found")

            # If 'WASTE' category is not found
            if index_to_update is None:
                print(f"No {category} category found in company_assignments.")
                exit()

            # Step 3: Construct the UpdateExpression and update the lastUpdated field for the found category
            update_expression = f"SET company_assignments[{index_to_update}].last_updated = :last_updated"

            # Step 4: Update the item in DynamoDB
            update_response = self.__table.update_item(
                Key={
                    PARTITION_KEY: company_id,
                    SORT_KEY: COMPANY_SORT_KEY_PREFIX,
                },
                UpdateExpression=update_expression,
                ExpressionAttributeValues={":last_updated": new_last_updated},
                ReturnValues="UPDATED_NEW",  # To get the updated values back in the response
            )

            print(update_response)
            return {"msg": "Update process completed..."}

        except ClientError as e:
            logger.exception(e)
            raise

    def get_country_for_energy_calculation(self, company_id, facility_id):
        # first find the location of the facility
        facilities = list(self.get_company_facilities(company_id))
        facility = next((f for f in facilities if f.facility_id == facility_id), None)
        if facility and facility.country_code:
            return facility.country_code
        # Next,
        company = self.get_company(company_id)
        if company and company.country_code:
            return company.country_code
        return None

    def get_facility_by_id(self, facility_id: str, company_id: str) -> Facility:
        response = self.__table.get_item(
            Key={
                PARTITION_KEY: company_id,
                SORT_KEY: FACILITY_SORT_KEY_PREFIX + facility_id,
            }
        )
        return _facility_from_dict(response["Item"])


def _company_to_dict(company: Company) -> dict:
    company_dict = company.model_dump(mode="json", exclude_none=True)
    company_dict.update(
        {
            PARTITION_KEY: company.company_id,
            SORT_KEY: COMPANY_SORT_KEY_PREFIX,
        }
    )
    return company_dict


def _company_from_dict(company_dict: dict) -> Company:
    return Company(**company_dict)


def _facility_to_dict(facility: Facility) -> dict:
    facility_dict = facility.model_dump(mode="json", exclude_none=True)
    facility_dict.update(
        {
            PARTITION_KEY: facility.company_id,
            SORT_KEY: FACILITY_SORT_KEY_PREFIX + facility.facility_id,
        }
    )
    return facility_dict


def _facility_from_dict(facility_dict: dict) -> Facility:
    return Facility(**facility_dict)


def _user_to_dict(user: User) -> dict:
    user_dict = user.model_dump(mode="json", exclude_none=True)
    user_dict.update(
        {
            PARTITION_KEY: user.company_id,
            SORT_KEY: USER_SORT_KEY_PREFIX + user.email,
        }
    )
    return user_dict


def _user_from_dict(user_dict: dict) -> User:
    return User(**user_dict)


@lru_cache
def get_company_repository() -> ICompanyRepository:
    """
    Always use this to fetch an instance of repository. It is cached.
    """
    return DDCompanyRepository()
