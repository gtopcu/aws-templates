

# https://sqlmodel.tiangolo.com/tutorial/connect/

from sqlmodel import Field, SQLModel, create_engine, Session

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")

"""
CREATE TABLE team (
    id INTEGER,
    name TEXT NOT NULL,
    headquarters TEXT NOT NULL,
    PRIMARY KEY (id)
)

CREATE TABLE hero (
    id INTEGER,
    name TEXT NOT NULL,
    secret_name TEXT NOT NULL,
    age INTEGER,
    team_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(team_id) REFERENCES team (id)
)
"""

if __name__ == "__main__":

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        team_1 = Team(name="team 1", headquarters="bar1")
        team_2 = Team(name="team 2", headquarters="bar2")
        session.add(team_1)
        session.add(team_2)
        session.commit()

        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team_id=1.id)
        session.refresh(hero_deadpond)
        print(hero_deadpond)
        

