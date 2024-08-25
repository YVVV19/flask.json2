from db import (
    Weather,
    Config,
)
from sqlalchemy import select
from main import get_response



def init_data():
    weather =(
        Weather(get_response())
    )
    with Config.SESSION.begin() as session:
        session.add_all(weather)