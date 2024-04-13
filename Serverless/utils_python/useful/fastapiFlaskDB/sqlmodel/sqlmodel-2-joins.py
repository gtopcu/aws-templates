
# https://sqlmodel.tiangolo.com/tutorial/connect/

from sqlmodel import Field, Session, SQLModel, create_engine, select #, update, insert, delete

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

        hero_deadpond = Hero(name="Deadpond", secret_name="Dive Wilson", team_id=team_1.id)
        session.add(hero_deadpond)
        session.commit()
        session.refresh(hero_deadpond)
        print(hero_deadpond)

        """
        SELECT hero.id, hero.name, team.name            
        FROM hero, team
        WHERE hero.team_id = team.id
        ----------------- SAME ----------------
        SELECT hero.id, hero.name, team.name
        FROM hero
        JOIN team
        ON hero.team_id = team.id
        """
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)

        """
        SELECT hero.id, hero.name, team.name
        FROM hero
        LEFT OUTER JOIN team (LEFT JOIN == LEFT OUTER JOIN)
        ON hero.team_id = team.id
        """
        statement = select(Hero, Team).join(Team, isouter=True)
        results = session.exec(statement)
        for hero, team in results:
            print("Hero:", hero, "Team:", team)

        statement = select(Hero, Team).join(Team).where(Team.name == "Preventers")
        results = session.exec(statement)
        for hero, team in results:
            print("Preventer Hero:", hero, "Team:", team)

        # Remove connection
        hero_deadpond.team_id = None
        session.add(hero_deadpond)
        session.commit()
        session.refresh(hero_spider_boy)
        print("No longer Preventer:", hero_spider_boy)    



