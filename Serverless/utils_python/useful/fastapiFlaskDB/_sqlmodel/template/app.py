
from sqlmodel import SQLModel

from .models import Hero, Team
from .database import engine, create_db_and_tables



def main() -> None:
    create_db_and_tables()

if __name__ == "__main__":
    main()
    #  python -m project.app