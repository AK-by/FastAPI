import datetime
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ExchangeRates.managers.ExchangeRatesManager import ExchangeRatesManager

app = FastAPI()
engine = create_engine("sqlite:///ExchangeRates/models/dz13.db", echo=True)
sessions = sessionmaker(bind=engine)
session = sessions()


@app.get("/")
def index():
    # Для теста, будем возвращать текущее время
    return datetime.datetime.now()


@app.get("/currencies")
def index():
    # Список доступных валют
    answer = "ISO 4217: "
    answer += "036 AUD Australian dollar, "
    answer += "978 EUR Euro, "
    answer += "643 RUB Russian ruble, "
    answer += "840 USD United States dollar"
    return answer


@app.get("/exchange-rates")
def exchange_rates():
    # Отображение всех курсов
    return ExchangeRatesManager.list(session=session)


@app.get("/exchange-rates/{currency_abbr}")
def exchange_rate(currency_abbr: str):
    # Отображение курсов по одной валюте
    return ExchangeRatesManager.get(session=session, currency_abbr=currency_abbr)


@app.post("/exchange-rates/add/{currency}")
def add_exchange_rates(currency: str):
    return ExchangeRatesManager.add(session=session, currency=currency)


@app.delete("/exchange-rates/delete/{id}")
def delete_exchange_rates(pk: int):
    return ExchangeRatesManager.remove(session=session, pk=pk)
