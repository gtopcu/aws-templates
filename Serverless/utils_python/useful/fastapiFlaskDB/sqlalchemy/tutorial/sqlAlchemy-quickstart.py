
# https://docs.sqlalchemy.org/en/20/orm/quickstart.html
# https://docs.sqlalchemy.org/en/20/tutorial/index.html#unified-tutorial
# https://docs.sqlalchemy.org/en/20/orm/cascades.html

from typing import Optional, List
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, ForeignKey, DateTime, Boolean, Integer, String
from sqlalchemy import select
from sqlalchemy.orm import Session, declarative_base, Mapped, mapped_column, relationship, backref

engine = create_engine('sqlite:///sqlite.db', echo=True)

# session = Session(engine)
# SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)

Base = declarative_base()

# Index('idx_user_email_age', User.email, User.age) # Composite index

class User(Base):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan" # https://docs.sqlalchemy.org/en/20/orm/cascades.html
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"), ondelete="CASCADE") 
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":

    with Session(engine) as session:

        # spongebob = User(
        #     name="spongebob",
        #     fullname="Spongebob Squarepants",
        #     addresses=[Address(email_address="spongebob@sqlalchemy.org")],
        # )
        # sandy = User(
        #     name="sandy",
        #     fullname="Sandy Cheeks",
        #     addresses=[
        #         Address(email_address="sandy@sqlalchemy.org"),
        #         Address(email_address="sandy@squirrelpower.org"),
        #     ],
        # )
        # patrick = User(name="patrick", fullname="Patrick Star")
        # session.add_all([spongebob, sandy, patrick])
        # session.commit()

        # stmt = select(User).where(User.name.in_(["spongebob", "sandy"]))
        # for user in session.scalars(stmt):
        #     print(user)

        # JOIN
        # SELECT address.id, address.email_address, address.user_id FROM address 
        # JOIN user_account ON user_account.id = address.user_id 
        # WHERE user_account.name = 'sandy' AND address.email_address = 'sandy@sqlalchemy.org'
        # stmt = (
        #     select(Address)
        #     .join(Address.user)
        #     .where(User.name == "sandy")
        #     .where(Address.email_address == "sandy@sqlalchemy.org")
        # )
        # sandy_address = session.scalars(stmt).one()
        # print(sandy_address)

        # # Update
        # stmt = select(User).where(User.name == "patrick")
        # patrick = session.scalars(stmt).one()
        # patrick.addresses.append(Address(email_address="patrickstar@sqlalchemy.org"))
        # sandy_address.email_address = "sandy_cheeks@sqlalchemy.org"
        # session.commit()

        # sandy = session.get(User, 2)
        # sandy.addresses.remove(sandy_address)
        # session.flush()

        # session.delete(patrick)
        pass