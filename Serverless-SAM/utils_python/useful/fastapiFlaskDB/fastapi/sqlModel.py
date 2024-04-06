
# https://sqlmodel.tiangolo.com/
# pip install sqlmodel

# Compatible with FastAPI, Pydantic and SQLAlchemy

from sqlmodel import Field, Session, SQLModel, create_engine, select, update, insert, delete
from decimal import Decimal

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# sqlite:// -> In Memory DB!

engine = create_engine(sqlite_url, echo=True) # echo: Print all SQL statements

class Hero(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    name: str = Field(default=None, index=True, max_length=50)
    age: int | None = Field(default=0, max_length=20)
    money: Decimal = Field(default=0, max_digits=5, decimal_places=3)
"""
CREATE TABLE hero (
        id INTEGER NOT NULL, 
        name VARCHAR NOT NULL, 
        age INTEGER, 
        money NUMERIC(5, 3) NOT NULL, 
        PRIMARY KEY (id)
)
CREATE INDEX ix_hero_name ON hero (name)
"""

def init_db():
    SQLModel.metadata.create_all(engine) # Creates tables for the models if not exists. Needs to run after model definitions

if __name__ == "__main__":
    init_db()

def create_heroes():
    hero = Hero(name="Spider-Boy", secret_name="Pedro Parqueador", money=0.001)
    with Session(engine) as session:
        session.add(hero)
        session.commit()

def select_heroes():
    with Session(engine) as session:
        statement = select(Hero).where(Hero.name == "Deadpond")
        # session.exec(statement).first()
        # session.exec(select(Hero)).all()
        results = session.exec(statement)
        hero = results.one()
        print("Hero mondy:", hero.money)

def all_methods():
    
    with Session(engine) as session:
        pass   
        # session.begin() # not necessary
        # session.flush() # not necessary
        # session.commit()
        # session.close()
        # session.close_all()
        # session.refresh()
        # session.reset()
        # session.prepare()
        # session.expire()
        # session.expire_all()
        # session.expunge()
        # session.expunge_all()

        # session.add(hero)
        # session.add_all([hero, hero])
        # session.delete(hero)
        # session.merge()

        # session.scalar(select(Hero).where(Hero.name == "Deadpond"))
        # session.scalars(select(Hero).where(Hero.name == "Deadpond"))



"""
CREATE TABLE hero (id INTEGER NOT NULL, name VARCHAR NOT NULL,)
CREATE INDEX ix_hero_name ON hero (name)

SELECT name FROM hero WHERE name = 'Deadpond'
INSERT INTO hero (id, name) VALUES (1, 'Deadpond')
UPDATE hero SET name = 'Deadpond' WHERE name = 'Deadpond'

DELETE FROM hero WHERE name = 'Deadpond'

TRUNCATE TABLE hero
DROP TABLE hero
"""