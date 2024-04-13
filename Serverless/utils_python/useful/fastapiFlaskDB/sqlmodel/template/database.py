

# https://sqlmodel.tiangolo.com/
# pip install sqlmodel

from sqlmodel import create_engine, SQLModel

sqlite_file_name = "sqlite.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
# sqlite:///:memory: -> memory DB

engine = create_engine(sqlite_url, echo=True)
# SessionLocal = sessionmaker(bind=engine) # autocommit=False, autoflush=False, expire_on_commit=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)