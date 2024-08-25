from sqlalchemy.orm import Mapped
from ..config import Config


class Weather:
    country: Mapped[str]
    city: Mapped[str]
    temperature: Mapped[int]
    condition: Mapped[str]