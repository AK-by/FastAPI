from typing import Any
from sqlalchemy.orm import Session


class ExchangeRatesCreateMixin:

    @staticmethod
    def insert(session: Session, table: Any, input_data: dict) -> Any:
        # Конструктор создания
        obj = table(**input_data)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj
