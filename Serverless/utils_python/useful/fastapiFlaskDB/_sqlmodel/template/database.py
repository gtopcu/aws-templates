

# https://sqlmodel.tiangolo.com/
# pip install sqlmodel

from sqlmodel import create_engine, SQLModel

sqlite_file_name = "sqlite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# engine = create_engine('sqlite:///:memory:', echo=True)
# engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# engine = create_engine('mysql+pymysql:///user:pwd@localhost/dbname', echo=True)

engine = create_engine(sqlite_url, echo=True)
# SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)