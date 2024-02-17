"""
class AwsDynamoDBClient:
    def __init__(self, aws_region: str = "us-east-2"):
        self._service = AwsServices.DYNAMODB
        self._resource = boto3.resource(
            self._service.value,
            region_name=aws_region,
        )

    def get_dynamodb_table_instance(self, table_name: str):
        return self._resource.Table(table_name)

    def _scan_or_query_table(
        self, query_or_scan_method, paginate, *args, **kwargs
    ):
        response = send_aws_http_request(
            self._service,
            query_or_scan_method,
            *args,
            **kwargs,
        )
        data = response["Items"]

        while paginate and "LastEvaluatedKey" in response:
            response = send_aws_http_request(
                self._service,
                query_or_scan_method,
                *args,
                ExclusiveStartKey=response["LastEvaluatedKey"],
                **kwargs,
            )
            data.extend(response["Items"])

        return data

    def query_table(self, table, *query_args, paginate=False, **query_kwargs):
        return self._scan_or_query_table(
            table.query, *query_args, paginate, **query_kwargs
        )

    def scan_table(self, table, *scan_args, paginate=False, **scan_kwargs):
        return self._scan_or_query_table(
            table.scan, *scan_args, paginate, **scan_kwargs
        )

    def update_item(self, table, *update_args, **update_kwargs):
        return send_aws_http_request(
            self._service,
            table.update_item,
            *update_args,
            **update_kwargs,
        )

    def create_item(self, table, *create_args, **create_kwargs):
        return send_aws_http_request(
            self._service,
            table.put_item,
            *create_args,
            **create_kwargs,
        )


class AwsDynamodbClient:
    def __init__(self, aws_region: str = "us-east-2"):
        self._service = AwsServices.DYNAMODB
        self._resource = boto3.resource(
            self._service.value,
            region_name=aws_region,
        )

    def get_dynamodb_table_instance(self, table_name: str):
        return self._resource.Table(table_name)

    def _scan_or_query_table(
        self, query_or_scan_method, paginate, *args, **kwargs
    ):
        response = send_aws_http_request(
            self._service,
            query_or_scan_method,
            *args,
            **kwargs,
        )
        data = response["Items"]

        while paginate and "LastEvaluatedKey" in response:
            response = send_aws_http_request(
                self._service,
                query_or_scan_method,
                *args,
                ExclusiveStartKey=response["LastEvaluatedKey"],
                **kwargs,
            )
            data.extend(response["Items"])

        return data

    def query_table(self, table, *query_args, paginate=False, **query_kwargs):
        return self._scan_or_query_table(
            table.query, *query_args, paginate, **query_kwargs
        )

    def scan_table(self, table, *scan_args, paginate=False, **scan_kwargs):
        return self._scan_or_query_table(
            table.scan, *scan_args, paginate, **scan_kwargs
        )

    def update_item(self, table, *update_args, **update_kwargs):
        return send_aws_http_request(
            self._service,
            table.update_item,
            *update_args,
            **update_kwargs,
        )

    def create_item(self, table, *create_args, **create_kwargs):
        return send_aws_http_request(
            self._service,
            table.put_item,
            *create_args,
            **create_kwargs,
        )
"""