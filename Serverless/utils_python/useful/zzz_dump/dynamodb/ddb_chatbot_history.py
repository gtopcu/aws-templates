import os
from uuid import uuid4

import boto3
from botocore.exceptions import ClientError
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.data_classes.appsync.scalar_types_utils import (
    aws_datetime,
)
from boto3.dynamodb.conditions import Key, Attr
from boto3.dynamodb.conditions import Equals, NotEquals, And, Or, Not, GreaterThan, GreaterThanEquals, LessThan, LessThanEquals 
from boto3.dynamodb.conditions import BeginsWith, Between, Contains, In, Size, AttributeExists, AttributeNotExists, AttributeType

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import (
    BaseMessage,
    message_to_dict,
    messages_from_dict,
    messages_to_dict,
)
from mypy_boto3_dynamodb.service_resource import Table

from enum import StrEnum
class ChatMessageSender(StrEnum): ...
class Conversation(): ...
class ConversationEvent(): ...
class ConversationSummary(): ...


logger = Logger()

DDB_TABLE_ENV = "CHATBOT_SESSION_DATA_TABLE"
PRIMARY_KEY = "PK"      # companyId::cognitoUserEmail
SORT_KEY = "SessionId"  # conversationId

client = boto3.resource("dynamodb")
ddb_table:Table = client.Table(os.environ[DDB_TABLE_ENV])


# Class is modified version of DynamoDBChatMessageHistory so that we can inject a timestamp to every saved message and session.
# We also want to be able to retrieve the last message and conversation as a serializable object.
class DynamoDBChatMessageHistoryWithTimestamp(BaseChatMessageHistory):
    """Chat message history that stores history in AWS DynamoDB.

    Args:
        session_id:   Arbitrary key that is used to store the messages of a single chat session.
        history_size: Maximum number of messages to store. If None then there is no limit. 
                      If not None then only the latest `history_size` messages are stored.
    """

    def __init__(
        self,
        session_id: str,
        key_name: str = "SessionId",
        key: dict[str, str] = None,
        history_size: int | None = 50,
    ):
        self.table = ddb_table
        self.session_id = session_id
        self.key: dict = key or {key_name: session_id}
        self.history_size = history_size

    @property
    def messages(self) -> list[BaseMessage]:
        """Retrieve the messages from DynamoDB. Used by AgentExecutor"""
        response = self._get_conversation()

        if response and "Item" in response:
            items = response["Item"]["History"]
        else:
            items = []

        messages = messages_from_dict(items)
        return messages

    def add_message(self, message: BaseMessage) -> None:
        """Append the message to the record in DynamoDB. Used by AgentExecutor"""
        # add id and timestamp to message
        message.id = str(uuid4())
        message.response_metadata.update({"timestamp": aws_datetime()})

        messages = messages_to_dict(self.messages)
        _message = message_to_dict(message)
        messages.append(_message)

        if self.history_size:
            messages = messages[-self.history_size:]

        try:
            self.table.put_item(
                Item={**self.key, "History": messages, "LastModified": aws_datetime()}
            )
        except ClientError as err:
            logger.error(err)

    @property
    def conversation(self) -> Conversation | None:
        response = self._get_conversation()

        if not response or "Item" not in response:
            return None

        _messages = response["Item"]["History"]
        messages = messages_from_dict(_messages)

        return Conversation(
            conversation_id=self.session_id,
            last_message_timestamp=response["Item"]["LastModified"],
            events=[
                ConversationEvent(
                    id=m.id,
                    timestamp=m.response_metadata["timestamp"],
                    conversation_id=self.session_id,
                    sender=_determine_sender(m.type),
                    message=m.content,
                )
                for m in messages
            ],
        )

    def _get_conversation(self) -> dict:
        try:
            response = self.table.get_item(Key=self.key)
        except ClientError as error:
            if error.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.warning("No record found with session id: %s", self.session_id)
            else:
                logger.error(error)
        return response

    def clear(self) -> None:
        """Clear all sessions from DynamoDB"""
        try:
            self.table.delete_item(Key=self.key)
        except ClientError as err:
            logger.error(err)


def get_chat_history(
    company_id: str, user_id: str, session_id: str
) -> DynamoDBChatMessageHistoryWithTimestamp:
    return DynamoDBChatMessageHistoryWithTimestamp(
        session_id=session_id,
        key={PRIMARY_KEY: _get_pk(company_id, user_id), "SessionId": session_id},
    )

def get_conversation_summaries_for_user(self, company_id: str, user_id: str) -> list[ConversationSummary]:
    response = self.table.query(
        KeyConditionExpression=Key(PRIMARY_KEY).eq(_get_pk(company_id, user_id)),
        ProjectionExpression="SessionId, LastModified",
    )

    if not response or "Items" not in response:
        return []

    conversations = response["Items"]
    return [
        ConversationSummary(
            conversation_id=c["SessionId"], last_message_timestamp=c["LastModified"]
        )
        for c in conversations
    ]


def _get_pk(company_id: str, user_id: str) -> str:
    return f"{company_id}::{user_id}"


def _determine_sender(_type: str) -> ChatMessageSender:
    if _type == "human":
        return ChatMessageSender.HUMAN
    elif _type == "ai":
        return ChatMessageSender.AI
    else:
        return ChatMessageSender.OTHER

