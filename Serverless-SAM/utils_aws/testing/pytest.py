# https://blog.newmathdata.com/advanced-unit-testing-in-aws-a666e787aa99

import pytest

# pytest -cov (include code coverage) -v(verbose) -s(prints outputs)
# pytest::test_function

# @pytest.fixture(scope="function") #scope can be function, class, module, session
def test_dynamo_put(create_table):
    pass

# Using pytest.mark.parametrize

def add(a, b):
    return a + b

# Testing the add function with various sets of parameters
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (4, 5, 9),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

# @pytest.mark.parametrize(
#     "value", ["foo", "bar", "baz"]
# )
# def test_dynamo_put(create_table, value):
#     dynamo_put("string", value)
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table("string")
#     response = table.get_item(
#         Key={
#             'string': value,
#             'mykey': 'foo'
#         }
#     )
#     print(response)
#     assert response["Item"]["string"] == value    