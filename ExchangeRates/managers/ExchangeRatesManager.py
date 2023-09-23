import requests
from datetime import datetime
from sqlalchemy.orm import Session
from ..mixins.ExchangeRatesCreate import ExchangeRatesCreateMixin
from ..mixins.ExchangeRatesRead import ExchangeRatesReadMixin
from ..mixins.ExchangeRatesDelete import ExchangeRatesDeleteMixin
from ..models.ExchangeRatesModel import Rates


class ExchangeRatesManager(ExchangeRatesReadMixin, ExchangeRatesCreateMixin, ExchangeRatesDeleteMixin):

    @classmethod
    def list(cls, session: Session):
        answer = []
        objects = cls.select_all(session=session, table=Rates)
        for o in objects:
            answer.append(
                {"ID": o.id,
                 "Abbr": o.Cur_Abbreviation,
                 "Scale": o.Cur_Scale,
                 "Rate": o.Cur_OfficialRate
                 }
            )
        return answer

    @classmethod
    def get(cls, session: Session, currency_abbr: str):
        answer = []
        objects = cls.select(session=session, table=Rates, currency_abbr=currency_abbr)
        for o in objects:
            answer.append(
                {"ID": o.id,
                 "Abbr": o.Cur_Abbreviation,
                 "Scale": o.Cur_Scale,
                 "Rate": o.Cur_OfficialRate
                 }
            )
        return answer

    @classmethod
    def add(cls, session: Session, currency: str):
        url = f"https://api.nbrb.by/exrates/rates/{currency}?parammode=1"
        result = requests.get(url)
        input_data = result.json()
        input_data["Date"] = datetime.strptime(input_data["Date"], '%Y-%m-%dT%H:%M:%S')
        cls.insert(session=session, table=Rates, input_data=input_data)
        return input_data

    @classmethod
    def remove(cls, session: Session, pk: int):
        return cls.delete(session=session, table=Rates, pk=pk)
