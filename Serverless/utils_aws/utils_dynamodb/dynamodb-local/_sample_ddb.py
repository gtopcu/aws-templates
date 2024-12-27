
# https://aws.github.io/chalice/tutorials/wschat.html

import os
import boto3
from boto3.dynamodb.conditions import Key, Attr

class UserTable:
    def __init__(self, table):
        self._table = table

    @classmethod
    def init_ddb_table(cls, table_name: str):
        # table_name = os.environ.get('DDB_TABLE', 'table-1')
        table = boto3.resource('dynamodb').Table(table_name)
        return cls(table)

    def list_rooms(self):
        r = self._table.scan()
        rooms = set([item['SK'].split('_', 1)[1] for item in r['Items'] if item['SK'].startswith('room_')])
        return rooms

    def set_room(self, connection_id, room):
        self._table.put_item(
            Item={
                'PK': connection_id,
                'SK': 'room_%s' % room,
            },
        )

    def remove_room(self, connection_id, room):
        self._table.delete_item(
            Key={
                'PK': connection_id,
                'SK': 'room_%s' % room,
            },
        )

    def get_connection_ids_by_room(self, room):
        r = self._table.query(
            IndexName='ReverseLookup',
            KeyConditionExpression=(
                Key('SK').eq('room_%s' % room)
            ),
            Select='ALL_ATTRIBUTES',
        )
        return [item['PK'] for item in r['Items']]

    def delete_connection(self, connection_id):
        r = self._table.query(
            KeyConditionExpression=(
                Key('PK').eq(connection_id)
            ),
            Select='ALL_ATTRIBUTES',
        )
        for item in r['Items']:
            self._table.delete_item(
                Key={
                    'PK': connection_id,
                    'SK': item['SK'],
                },
            )

    def get_record_by_connection(self, connection_id):
        r = self._table.query(
            KeyConditionExpression=(
                Key('PK').eq(connection_id)
                
            ),
            Select='ALL_ATTRIBUTES',
        )
        r = {
            entry['SK'].split('_', 1)[0]: entry['SK'].split('_', 1)[1] for entry in r['Items']
        }
        return r

mytable: UserTable = UserTable.init_ddb_table('table-1')