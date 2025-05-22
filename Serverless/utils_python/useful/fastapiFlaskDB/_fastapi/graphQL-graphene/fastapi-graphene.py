
# https://www.youtube.com/watch?v=ZUrNFhG3LK4
# https://www.youtube.com/watch?v=77YWE5-Q8vs

# https://graphene-python.org/
# https://docs.graphene-python.org/projects/sqlalchemy/en/latest/

# pip install -U fastapi graphene
# pip install graphene

# pip install --pre "graphene-sqlalchemy"
# pip install starlette_graphene3 - do not use

"""
import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return 'World'

schema = graphene.Schema(query=Query)
schema.execute('''
  query {
    hello
  }
''')
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from logging import getLogger
# from starlette_graphene3 import GraphQLApp, make_graphql_handler


logger = getLogger(__name__)

app = FastAPI()

app.add_middleware(
   CORSMiddleware,
   allow_origins=["*"],
   allow_credentials=True,
   allow_methods=["*"],
   allow_headers=["*"],
)

# app.add_route("/graphql", GraphQLApp(schema=AppSchema, on_get=make_graphql_handler))

@app.get("/healthcheck/")
def get_healthcheck():
    return "Status: OK!"