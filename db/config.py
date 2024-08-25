from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Config:
    ENGINE = create_engine(
        "sqlite:///my_db.sql"
    )

    SESSION = sessionmaker(bind=ENGINE)

