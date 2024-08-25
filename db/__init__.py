from .config import Config
from .models import (
    Base,
    Weather,
)


def migrate():
    Base.metadata.drop_all(Config.ENGINE)
    Base.metadata.create_all(Config.ENGINE)