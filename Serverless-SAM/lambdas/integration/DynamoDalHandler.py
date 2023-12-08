
import boto3
from boto3.dynamodb.conditions import Attr
import DbHandler

# Utilizing the adapter pattern
class DynamoDalHandler(DbHandler):
    def __init__(self, table_name):
        self.table_name = table_name
        self.table = boto3.resource('dynamodb').Table(table_name)

    def get_item(self, key):
        return self.table.get_item(Key=key)

    def put_item(self, item):
        self.table.put_item(Item=item)

    def delete_item(self, key):
        self.table.delete_item(Key=key)

    def query_items(self, key, value):
        return self.table.query(KeyConditionExpression=Key(key).eq(value))

    def scan_items(self, key, value):
        return self.table.scan(FilterExpression=Attr(key).eq(value))

    def update_item(self, key, value, update_expression, expression_attribute_values):
        self.table.update_item(Key=key, UpdateExpression=update_expression, ExpressionAttributeValues=expression_attribute_values)

    def get_all_items(self):
        pass