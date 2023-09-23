from typing import Any
from sqlalchemy import select
from sqlalchemy.orm import Session


class ExchangeRatesReadMixin:

    @classmethod
    def select_all(cls, session: Session, table: Any):
        # Конструктор чтения
        query = select(table)
        objects = session.execute(query)
        return objects.scalars().all()

    @classmethod
    def select(cls, session: Session, table: Any, currency_abbr: str):
        # Конструктор чтения
        query = select(table).where(table.Cur_Abbreviation == currency_abbr)
        objects = session.execute(query)
        return objects.scalars().all()
