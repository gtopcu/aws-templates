
from sqlalchemy import create_engine, MetaData, Table, ForeignKey, Column, DateTime, Boolean, Integer, String
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker, Session, declarative_base, Mapped, mapped_column, relationship

from datetime import datetime
import hashlib
import os

engine = create_engine('sqlite:///sqlite.db', echo=True)
SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)
Base = declarative_base()
# metadata = MetaData() # database schema


class User(Base):
    """
    CREATE TABLE users (
        id INTEGER NOT NULL, 
        PRIMARY KEY (id)
    )
    """
    __tablename__ = "users"
    # __table_args__ = {"extend_existing": True}

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    auth: Mapped["UserAuth"] = relationship("UserAuth", uselist=False, back_populates="user") 
    posts: Mapped[list["UserPost"]] = relationship("UserPost", back_populates="user")
    
    def __init__(self, username:str, email:str, password:str):
        super().__init__()
        self.auth = UserAuth(username=username, email=email)
        self.auth.set_password(password)
    
    def __repr__(self) -> str:
        return f"<User(username={self.auth.username}, email={self.auth.email})>"


# 1-to-1 
class UserAuth(Base):
    """
    CREATE TABLE user_auth (
        id INTEGER NOT NULL, 
        username VARCHAR(50) NOT NULL, 
        email VARCHAR(100) NOT NULL, 
        password_hash VARCHAR(64) NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(id) REFERENCES users (id)
    )
    CREATE UNIQUE INDEX ix_user_auth_email ON user_auth (email)
    """
    __tablename__ = "user_auth"

    id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    username: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(100), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(64))
    user: Mapped["User"] = relationship("User", back_populates="auth")

    def __init__(self, username:str, email:str):
        self.username = username
        self.email = email

    def set_password(self, password:str) -> None:
        self.password_hash = hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password:str) -> bool:
        return self.password_hash == hashlib.sha256(password.encode()).hexdigest()

    def __repr__(self) -> str:
        return f"<UserAuth(username={self.username}, email={self.email})>"

# 1-to-many
class UserPost(Base):
    """
    CREATE TABLE user_posts (
        id INTEGER NOT NULL, 
        user_id INTEGER NOT NULL, 
        content VARCHAR(1000) NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(user_id) REFERENCES users (id)
    )
    CREATE INDEX ix_user_posts_user_id ON user_posts (user_id)   
    """
    __tablename__ = "user_posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    content: Mapped[str] = mapped_column(String(1000))
    user: Mapped["User"] = relationship("User", back_populates="posts")

    def __repr__(self) -> str:
        return f"<UserPost(user_id={self.user}, content={self.content})>"


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)


if __name__ == "__main__":

    with SessionLocal.begin() as session:
        user = User(username="gokhan", email="gtopcu@gmail.com", password="123456")
        post1 = UserPost(content="test content1", user=user)
        post2 = UserPost(content="test content2", user=user)
        session.add(user)
        session.add(post1)
        session.add(post2)

    with SessionLocal.begin() as session:
        user = session.query(User).first()
        print(user)
        print(user.auth)
        print(user.posts)
        #print(print(user.posts[0]))
        print(user.auth.check_password("1234567"))
        print(user.auth.check_password("123456"))
        
        # session.delete(user.auth)
        # session.delete(user)

        # os.system("clear")
        posts = session.query(UserPost).filter(UserPost.user==user).all()
        print(posts)
