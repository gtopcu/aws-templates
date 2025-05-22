
from graphene import ObjectType, String, UUID, ID, Boolean, BigInt, Int, Float, Decimal, Date, DateTime, Time
from graphene import Field, List, NonNull, Base64, JSONString, Enum
from graphene import Schema, Mutation

from uuid import uuid4

class User(ObjectType):
    id = String()
    name = String()
    age = Int()

users = [
    {
        "id": UUID(str(uuid4())),
        "name": "Gokhan",
        "age": 40
    }
]

class Query(ObjectType):
    def resolve_get_user(root, info, id:str):
        return list(filter(lambda user: user["id"]==id))[0]
    
    def resolve_get_users(root, info):
        return users

class CreateUser(Mutation):
    class Arguments:
        id = String()
        name = String()
        age = Int()
    user = Field(lambda: User)

    def mutate(root, info, id, name, age):
        user = User(id=id, name=name, age=age)
        # users.append(user)
        users.append({
           "id": id,
           "name": name,
           "age": age,
       })
        return CreateUser(user=user)

class UpdateUser(Mutation):
   class Arguments:
       id = String()
       name = String()
       age = Int()
   user = Field(lambda: User)
   
   def mutate(root, info, id, name, age):
      old_user = list(filter(lambda user: user["id"]==id))[0]
      user = User(id=old_user["id"], name=old_user["name"], age=old_user["age"])
      users.remove(old_user)
      return UpdateUser(user=user)
   
class DeleteUser(Mutation):
   class Arguments:
    id = String()
    user = Field(lambda: User)
   
   def mutate(root, info, id):
       old_user = list(filter(lambda user: user["id"] == id))[0]
       user = User(id=old_user["id"], name=old_user["name"], age=old_user["age"])
       users.remove(old_user)
       return DeleteUser(user=user)
   
class MyMutations(ObjectType):
   create_user = CreateUser.Field()
   update_user = UpdateUser.Field()
   delete_user = DeleteUser.Field()

class MyQuery(Query):
   user = Field(User)
   get_user = Field(User, id=String())
   get_users = List(User)

schema = Schema(query=MyQuery, mutation=MyMutations)


result = schema.execute(
   """
   query {
       getUser(id: "1") {
           id
           name
           age
       }
   }
   """
)
print(result.data)

result = schema.execute(
   """
   query {
       getUsers {
           id
           name
           age
       }
   }
   """
)
print(result.data)

result = schema.execute(
   """
   mutation {
       createUser(id: "1", name: "Gokhan Topcu", age: 1) {
           user {
               id
               name
               age
           }
       }
   }
   """
)
print(result.data)

result = schema.execute(
   """
   mutation {
       updateUser(id: "1", name: "S. Gokhan Topcu", age: 40) {
           user {
               id
               name
               age
           }
       }
   }
   """
)
print(result.data)

result = schema.execute(
   """
   mutation {
       deleteUser(id: "1") {
           user {
               id
               name
               age
           }
       }
   }
   """
)
print(result.data)