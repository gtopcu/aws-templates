
# https://www.youtube.com/watch?v=bEdr8WZmP8o
# https://httpie.io/
# pip install fastapi uvicorn strawberry-graphql httpie

# http://0.0.0.0:8000/docs
# http://0.0.0.0:8000/openapi.json
# http://0.0.0.0:8000/graphql

# query MoviesSchema {
#   __schema {
#     description
#   }
# }
# query MoviesType {
# 	  __typename
# }
# query Movies {
# 	movies(limit: 10, offset: 1) {
#      title,
#      director
#   }
# }

from fastapi import FastAPI
import strawberry
from strawberry.asgi import GraphQL
import asyncio
from typing import Optional


@strawberry.type
class Movie:
    title: str
    director: str
    country: str | None = None
    # country: Optional[str] = None

@strawberry.type
class Query:
    @strawberry.field
    def movies(self, limit: int, offset: int) -> list[Movie]:
        movies = [
            Movie(title="The Shawshank Redemption", director="Frank Darabont"),
            Movie(title="The Godfather", director="Francis Ford Coppola"),
            Movie(title="The Dark Knight", director="Christopher Nolan"),
            Movie(title="12 Angry Men", director="Sidney Lumet"),
            Movie(title="Schindler's List", director="Steven Spielberg"),
        ]
        print("Limit: ", limit, " Offset: ", offset)
        return movies

schema = strawberry.Schema(query=Query)
app = FastAPI()
app.add_route("/graphql", GraphQL(schema, debug=True))

@app.get("/")
def root():
    return {"message": "Welcome to strawberry GraphQL API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def add_movie(self, title: str, director: str) -> Movie:
#         movie = Movie(title=title, director=director)
#         return movie

# @strawberry.type
# class Subscription:
#     @strawberry.subscription
#     async def count(self, target: int = 100):
#         for i in range(target):
#             yield i
#             await asyncio.sleep(0.5)
