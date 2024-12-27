

# https://sqlmodel.tiangolo.com/tutorial/relationship-attributes/define-relationships-attributes/

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select #, update, insert, delete

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="team")


class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    team_id: int | None = Field(default=None, foreign_key="team.id")
    team: Team | None = Relationship(back_populates="heroes")

"""

"""

if __name__ == "__main__":

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:

        hero_black_lion = Hero(name="Black Lion", secret_name="Trevor Challa", age=35)
        hero_sure_e = Hero(name="Princess Sure-E", secret_name="Sure-E")
        team_wakaland = Team(
            name="Wakaland",
            headquarters="Wakaland Capital City",
            heroes=[hero_black_lion, hero_sure_e],
        )
        # team_preventers.heroes.append(hero_tarantula)
        session.add(team_wakaland)
        session.commit()
        session.refresh(team_wakaland)
        print("Team Wakaland:", team_wakaland)

        # SELECT
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()
        print("Spider-Boy's team again:", hero_spider_boy.team)

        # SELECT MANY
        statement = select(Team).where(Team.name == "Preventers")
        result = session.exec(statement)
        team_preventers = result.one()
        print("Preventers heroes:", team_preventers.heroes)

        # Remove Relationship
        statement = select(Hero).where(Hero.name == "Spider-Boy")
        result = session.exec(statement)
        hero_spider_boy = result.one()
        hero_spider_boy.team = None
        session.add(hero_spider_boy)
        session.commit()
        session.refresh(hero_spider_boy)
        print("Spider-Boy without team:", hero_spider_boy)

        """
        back_populates
        Tells SQLModel that if something changes in this model, it should change that attribute in the other model, 
        and it will work even before committing with the session (that would force a refresh of the data).
        """
        hero_spider_boy = session.exec(
            select(Hero).where(Hero.name == "Spider-Boy")
        ).one()

        preventers_team = session.exec(
            select(Team).where(Team.name == "Preventers")
        ).one()