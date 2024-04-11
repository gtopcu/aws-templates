
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html
# https://docs.sqlalchemy.org/en/20/orm/session_basics.html
# https://docs.sqlalchemy.org/en/20/orm/declarative_tables.html#orm-declarative-mapped-column-type-map
# https://docs.sqlalchemy.org/en/20/orm/cascades.html

from typing import Optional

# from sqlalchemy import Table, Column
from sqlalchemy import create_engine, Integer, String
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column, relationship, backref

engine = create_engine('sqlite:///sqlite.db', echo=True)

class Base(DeclarativeBase):
    pass

#!!! mapped_column() supersedes the use of Column() !!!

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    fullname: Mapped[Optional[str]]
    nickname: Mapped[Optional[str]] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r}, nickname={self.nickname!r})"

# # equivalent Table object produced
# user_table = Table(
#     "user",
#     Base.metadata,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(50)),
#     Column("fullname", String()),
#     Column("nickname", String(30)),
# )

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":

    with Session(engine) as session:
        user = User(name="gokhan", fullname="Gokhan Goknur", nickname="gokhan")
        session.add(user)
        session.commit()

        # user = session.query(User).first()
        # user = session.query(User).filter(User.name == "gokhan").first()
        # print(user)
        # print(user.name)
        # print(user.fullname)
        # print(user.nickname)
        
        for user in session.query(User).all():
            print(user)

        # session.query(User).filter(User.name == "gokhan").update({"fullname": "Gokhan Goknur"})
        # session.query(User).filter(User.name == "gokhan").delete()
        # session.delete(user)


        