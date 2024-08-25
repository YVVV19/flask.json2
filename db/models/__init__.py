from __future__ import annotations

from sqlalchemy.orm import (
    DeclarativeBase, 
    Mapped, 
    mapped_column, 
    )

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def get_model_by_name(model_name: str):
    models = {
        str(Weather): Weather,
    }
    models.get(model_name)


from .weather import Weather
