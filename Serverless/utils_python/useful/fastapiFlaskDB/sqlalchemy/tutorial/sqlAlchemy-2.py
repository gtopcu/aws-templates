
from typing import Optional
from sqlalchemy import create_engine, MetaData, Table, Column, DateTime, Boolean, Integer, String
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, Session, declarative_base, Mapped, mapped_column, relationship

from datetime import datetime

engine = create_engine('sqlite:///sqlite.db', echo=True)
SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)
Base = declarative_base()
# metadata = MetaData() # database schema


class User(Base):
    """
    CREATE TABLE users (
        id INTEGER NOT NULL, 
        name VARCHAR(100) NOT NULL, 
        title VARCHAR, 
        address_id INTEGER NOT NULL, 
        working BOOLEAN NOT NULL, 
        updated DATETIME NOT NULL, 
        PRIMARY KEY (id)
    )
    CREATE UNIQUE INDEX ix_users_name ON users (name)
    """
    __tablename__ = "users"
    # __table_args__ = {"extend_existing": True}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), index=True, unique=True, nullable=False)
    title: Mapped[Optional[str]]
    address_id: Mapped[int] = mapped_column(default=0)
    working: Mapped[bool] = mapped_column(default=False)
    updated: Mapped[datetime] = mapped_column(default=datetime.now())

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, address_id={self.address_id}, title={self.title} \
                        working={self.working}, updated={self.updated})"

Base.metadata.create_all(bind=engine)
# Base.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    
    # with engine.connect() as conn:
    #     with conn.begin() as trans:
    #         conn.execute(table.insert(), {"username": "sandy"})

    user1 = User(name = "gokhan", address_id=1, working=True)
    user2 = User(name = "goknur")
    
    with SessionLocal() as session:
        session.add(user1)
        session.add(user2)
        session.commit()
        session.refresh(user1)

        # session.query(User).filter(User.name == "gokhan").update({"address_id": 2})
        for user in session.query(User).all():
            print(repr(user))


