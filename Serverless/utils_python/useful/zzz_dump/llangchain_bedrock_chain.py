
import time
from functools import lru_cache

import boto3
from botocore.config import Config
from aws_lambda_powertools import Logger

from langchain_aws import ChatBedrock
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


logger = Logger()


class BedrockWrapper:
    def __init__(
        self,
        model_id: str,
        max_tokens: int,
        prompt_stop_sequence: list[str],
        region_name: str,
    ):
        config = Config(
            region_name=region_name, retries={"max_attempts": 3, "mode": "standard"}
        )
        client = boto3.client(service_name="bedrock-runtime", config=config)
        self.__bedrock = _set_up_bedrock(client, model_id, max_tokens, prompt_stop_sequence)

    def invoke_bedrock(
        self, query: list[tuple[str, str]], variables: dict[str, str]
    ) -> str:
        # Invoke Example
        template = ChatPromptTemplate.from_messages(query)

        chain = template | self.__bedrock | StrOutputParser()

        retry_time = 10
        response = None
        while retry_time <= 60:
            try:
                logger.info("Calling bedrock...")
                logger.debug(f"query = {query}")
                logger.debug(f"variables = {variables}")
                # Chain Invoke
                response = chain.invoke(variables)
                logger.info("Got response.")
                break
            except ValueError as e:
                if "ThrottlingException" in str(e):
                    logger.exception(
                        f"ThrottlingException. Retrying in {retry_time} seconds..."
                    )
                    time.sleep(retry_time)
                    retry_time += 20
                else:
                    raise e
        if response is None:
            raise Exception("Throttled too many times.")
        logger.debug(f"Data from Bedrock: {response}")
        return response


def _set_up_bedrock(client, model_id: str, max_tokens: int, stop_sequences: list[str]):
    # Setup inference modifier and Bedrock LLM
    model_kwargs = {
        "temperature": 0,
        "stop_sequences": stop_sequences,
        "max_tokens": max_tokens,
    }

    # Initialize Bedrock LLM
    bedrock_llm = ChatBedrock(
        credentials_profile_name="bedrock-admin",
        client=client,
        model_id=model_id,
        model_kwargs=model_kwargs,
    )
    return bedrock_llm


# TODO - fix hardcoded param
@lru_cache
def get_bedrock(
    prompt_stop_sequence: str,
    max_tokens: int | None = 4000,
    model_id: str | None = "anthropic.claude-v2:1",
    region_name: str | None = "eu-central-1",
):
    return BedrockWrapper(model_id, max_tokens, [prompt_stop_sequence], region_name)
