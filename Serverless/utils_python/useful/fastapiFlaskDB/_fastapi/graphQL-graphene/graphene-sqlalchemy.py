
# https://www.youtube.com/watch?v=ZUrNFhG3LK4
# https://www.youtube.com/watch?v=77YWE5-Q8vs

# https://graphene-python.org/
# https://docs.graphene-python.org/projects/sqlalchemy/en/latest/

# pip install -U fastapi graphene
# pip install graphene

# pip install --pre "graphene-sqlalchemy"

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)


import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel
        # use `only_fields` to only expose specific fields ie "name"
        # only_fields = ("name",)
        # use `exclude_fields` to exclude specific fields ie "last_name"
        # exclude_fields = ("last_name",)

class Query(graphene.ObjectType):
    users = graphene.List(User)

    def resolve_users(self, info):
        query = User.get_query(info)  # SQLAlchemy query
        return query.all()

schema = graphene.Schema(query=Query)

query = '''
    query {
      users {
        name,
        lastName
      }
    }
'''
# result = schema.execute(query, context_value={'session': db_session})


# It's important to provide a session for graphene-sqlalchemy to resolve the models. Here, it is provided using the GraphQL context. 
# You may also subclass SQLAlchemyObjectType by providing abstract = True in your subclasses Meta:
# from graphene_sqlalchemy import SQLAlchemyObjectType

# class ActiveSQLAlchemyObjectType(SQLAlchemyObjectType):
#     class Meta:
#         abstract = True

#     @classmethod
#     def get_node(cls, info, id):
#         return cls.get_query(info).filter(
#             and_(cls._meta.model.deleted_at==None,
#                  cls._meta.model.id==id)
#             ).first()

# class User(ActiveSQLAlchemyObjectType):
#     class Meta:
#         model = UserModel

# class Query(graphene.ObjectType):
#     users = graphene.List(User)

#     def resolve_users(self, info):
#         query = User.get_query(info)  # SQLAlchemy query
#         return query.all()

# schema = graphene.Schema(query=Query)

