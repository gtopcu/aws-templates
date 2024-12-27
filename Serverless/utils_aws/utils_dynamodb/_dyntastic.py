
# https://pypi.org/project/dyntastic/
# pip install dyntastic

import uuid
from datetime import datetime
from typing import Optional

from dyntastic import Dyntastic
from dyntastic.exceptions import DoesNotExist
from dyntastic import A # A is shorthand for the Attr class

from pydantic import Field

# Dyntastic is a subclass of Pydantic's BaseModel, so can be used in all the same places a 
# Pydantic model can be used (FastAPI, etc)

class Product(Dyntastic):
    __table_name__ = "products"
    __hash_key__ = "product_id"

    product_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class Event(Dyntastic):
    __table_name__ = "events"
    __hash_key__ = "event_id"
    __range_key__ = "timestamp"

    event_id: str
    timestamp: datetime
    data: dict


p = Product(name="bread", price=3.49)
print(p)
# Product(product_id='d2e91c30-e701-422f-b71b-465b02749f18', name='bread', description=None, price=3.49, tax=None)
print(p.model_dump())
# {'product_id': 'd2e91c30-e701-422f-b71b-465b02749f18', 'name': 'bread', 'description': None, 'price': 3.49, 'tax': None}
print(p.model_dump_json())
# '{"product_id": "d2e91c30-e701-422f-b71b-465b02749f18", "name": "bread", "description": null, "price": 3.49, "tax": null}'


# Insert Items ------------------------------------------------------------------------

product = Product(name="bread", description="Sourdough Bread", price=3.99)
product.product_id
# d2e91c30-e701-422f-b71b-465b02749f18

# Nothing is written to DynamoDB until .save() is called:
product.save()


# Getting Items ------------------------------------------------------------------------

try: 
    Product.get("d2e91c30-e701-422f-b71b-465b02749f18", consistent_read=True)
    # Product(product_id='d2e91c30-e701-422f-b71b-465b02749f18', name='bread', description="Sourdough Bread", price=3.99, tax=None)
    Event.get("d2e91c30-e701-422f-b71b-465b02749f18", "2022-02-12T18:27:55.837Z")
except DoesNotExist as e:
    print("Item does not exist")

# Safe Get - returns None if item does not exist
Product.safe_get("nonexistent")


# Querying ------------------------------------------------------------------------

# auto paging iterable
for event in Event.query("some_event_id"):
    print(event)

Event.query("some_event_id", per_page=10)
Event.query("some_event_id")
Event.query("some_event_id", range_key_condition=A.timestamp < datetime(2022, 2, 13))
Event.query("some_event_id", filter_condition=A.some_field == "foo")

# query an index
Event.query(A.my_other_field == 12345, index="my_other_field-index")

# note: Must provide a condition expression rather than just the value
Event.query(123545, index="my_other_field-index")  # errors!

# query an index with an optional filter expression
filter_expression = None
filter_value = 12345

if filter_value:
    filter_expression = A('filter_field').eq(filter_value)
Event.query(
    A.my_other_field == 12345,
    index="my_other_field-index",
    filter_expression=filter_expression
)

# consistent read
Event.query("some_event_id", consistent_read=True)

# specifies the order for index traversal, the default is ascending order
# returns the results in the order in which they are stored by sort key value
Event.query("some_event_id", range_key_condition=A.version.begins_with("2023"), scan_index_forward=False)


# DynamoDB Indexes using a KEYS_ONLY or INCLUDE projection are supported:

for event in Event.query("2023-09-22", index="date-keys-only-index"):
    event.id
    # "..."
    event.timestamp
    # datetime(...)

    event.data
    # ValueError: Dyntastic instance was loaded from a KEYS_ONLY or INCLUDE index.
    #             Call refresh() to load the full item, or pass load_full_item=True
    #             to query() or scan()

# automatically fetch the full items
for event in Event.query("2023-09-22", index="date-keys-only-index", load_full_item=True):
    event.data
    # {...}

# If you need to manually handle pagination, use query_page:

page = Event.query_page(...)
page.items
# [...]
page.has_more
# True
page.last_evaluated_key
# {"event_id": "some_event_id", "timestamp": "..."}

Event.query_page(..., last_evaluated_key=page.last_evaluated_key)


# Scanning is done identically to querying, except there are no hash key or range key conditions.

# auto paging iterable
for event in Event.scan():
    pass

Event.scan((A.my_field < 5) & (A.some_other_field.is_in(["a", "b", "c"])))
Event.scan(..., consistent_read=True)


# Updating Items in DynamoDB

my_item.update(A.my_field.set("new_value"))
my_item.update(A.my_field.set(A.another_field))
my_item.update(A.my_int.set(A.another_int - 10))
my_item.update(A.my_int.set(A.my_int + 1))
my_item.update(A.my_list.append("new_element"))
my_item.update(A.some_attribute.set_default("value_if_not_already_present"))

my_item.update(A.my_field.remove())
my_item.update(A.my_list.remove(2))  # remove by index

my_item.update(A.my_string_set.add("new_element"))
my_item.update(A.my_string_set.add({"new_1", "new_2"}))
my_item.update(A.my_string_set.delete("element_to_remove"))
my_item.update(A.my_string_set.delete({"remove_1", "remove_2"}))

# Multiple updates can be performed at once
my_item.update(
    A.my_field.set("new_value"),
    A.my_int.set(A.my_int + 1),
    ...
)
# The data is automatically refreshed after the update request. To disable this behavior, pass refresh=False:
my_item.update(..., refresh=False)

# Supports conditions
my_item.update(..., condition=A.my_field == "something")

# By default, if the condition is not met, the update call will be a noop. To instead error in this situation, 
# pass require_condition=True:

my_item.update(..., require_condition=True)
