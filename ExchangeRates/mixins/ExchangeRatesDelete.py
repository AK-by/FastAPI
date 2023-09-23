from typing import Any
from sqlalchemy import delete
from sqlalchemy.orm import Session


class ExchangeRatesDeleteMixin:

    @staticmethod
    def delete(session: Session, table: Any, pk: int) -> Any:
        # Конструктор удаления
        query = delete(table).where(table.id == pk)
        session.execute(query)
        session.commit()
        return f"Deleted id={pk}"
