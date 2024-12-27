
# https://sqlmodel.tiangolo.com/tutorial/many-to-many/

from sqlmodel import Field, Relationship, Session, SQLModel, create_engine, select #, update, insert, delete

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo=True)


# Link/Adjacent/Junction Table
class HeroTeamLink(SQLModel, table=True):
    team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
    hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)

class Team(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    headquarters: str
    heroes: list["Hero"] = Relationship(back_populates="teams", link_model=HeroTeamLink)

class Hero(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: int | None = Field(default=None, index=True)
    teams: list[Team] = Relationship(back_populates="heroes", link_model=HeroTeamLink)

"""
CREATE TABLE team (
        id INTEGER,
        name VARCHAR NOT NULL,
        headquarters VARCHAR NOT NULL,
        PRIMARY KEY (id)
)
CREATE TABLE hero (
        id INTEGER,
        name VARCHAR NOT NULL,
        secret_name VARCHAR NOT NULL,
        age INTEGER,
        PRIMARY KEY (id)
)
CREATE TABLE heroteamlink (
        team_id INTEGER,
        hero_id INTEGER,
        PRIMARY KEY (team_id, hero_id),
        FOREIGN KEY(team_id) REFERENCES team (id),
        FOREIGN KEY(hero_id) REFERENCES hero (id)
)
"""

if __name__ == "__main__":

    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        
        team_preventers = Team(name="Preventers", headquarters="Sharp Tower")
        team_z_force = Team(name="Z-Force", headquarters="Sister Margaret's Bar")

        hero_deadpond = Hero(
            name="Deadpond",
            secret_name="Dive Wilson",
            teams=[team_z_force, team_preventers],
        )
        hero_rusty_man = Hero(
            name="Rusty-Man",
            secret_name="Tommy Sharp",
            age=48,
            teams=[team_preventers],
        )
        hero_spider_boy = Hero(
            name="Spider-Boy", secret_name="Pedro Parqueador", teams=[team_preventers]
        )

        session.add(hero_deadpond)
        session.add(hero_rusty_man)
        session.add(hero_spider_boy)
        session.commit()

        session.refresh(hero_deadpond)
        session.refresh(hero_rusty_man)
        session.refresh(hero_spider_boy)

        print("Deadpond:", hero_deadpond)
        print("Deadpond teams:", hero_deadpond.teams)
        print("Rusty-Man:", hero_rusty_man)
        print("Rusty-Man Teams:", hero_rusty_man.teams)
        print("Spider-Boy:", hero_spider_boy)
        print("Spider-Boy Teams:", hero_spider_boy.teams)
        

        # Update
        hero_spider_boy = session.exec(
            select(Hero).where(Hero.name == "Spider-Boy")
        ).one()
        team_z_force = session.exec(select(Team).where(Team.name == "Z-Force")).one()

        team_z_force.heroes.append(hero_spider_boy)
        session.add(team_z_force)
        session.commit()

        # Because we are accessing an attribute in the models right after we commit,
        # the data is refreshed automatically do we don't have to call session.refresh()
        print("Updated Spider-Boy's Teams:", hero_spider_boy.teams)
        print("Z-Force heroes:", team_z_force.heroes)
        """
        Notice that we only add Z-Force to the session, then we commit.
        We never add Spider-Boy to the session, and we never even refresh it. But we still print his teams.
        This still works correctly because we are using back_populates in the Relationship() in the models.     
        That way, SQLModel (actually SQLAlchemy) can keep track of the changes and updates, and make sure they 
        also happen on the relationships in the other related models
        """

        # Remove connection
        hero_spider_boy.teams.remove(team_z_force)
        session.add(team_z_force)
        session.commit()

        print("Reverted Z-Force's heroes:", team_z_force.heroes)
        print("Reverted Spider-Boy's teams:", hero_spider_boy.teams)


        """
        Link with additional fields - https://sqlmodel.tiangolo.com/tutorial/many-to-many/link-with-extra-fields/

        class HeroTeamLink(SQLModel, table=True):
            team_id: int | None = Field(default=None, foreign_key="team.id", primary_key=True)
            hero_id: int | None = Field(default=None, foreign_key="hero.id", primary_key=True)
            is_training: bool = False
            team: "Team" = Relationship(back_populates="hero_links")
            hero: "Hero" = Relationship(back_populates="team_links")

        class Team(SQLModel, table=True):
            id: int | None = Field(default=None, primary_key=True)
            name: str = Field(index=True)
            headquarters: str
            hero_links: list[HeroTeamLink] = Relationship(back_populates="team")

        class Hero(SQLModel, table=True):
            id: int | None = Field(default=None, primary_key=True)
            name: str = Field(index=True)
            secret_name: str
            age: int | None = Field(default=None, index=True)
            team_links: list[HeroTeamLink] = Relationship(back_populates="hero")

        deadpond_team_z_link = HeroTeamLink(team=team_z_force, hero=hero_deadpond)
        deadpond_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_deadpond, is_training=True
        )
        spider_boy_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_spider_boy, is_training=True
        )
        rusty_man_preventers_link = HeroTeamLink(
            team=team_preventers, hero=hero_rusty_man
        )
        session.add(deadpond_team_z_link)
        session.add(deadpond_preventers_link)
        session.add(spider_boy_preventers_link)
        session.add(rusty_man_preventers_link)
        session.commit()

        """


