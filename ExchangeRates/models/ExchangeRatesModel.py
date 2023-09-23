from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

Base = declarative_base()


class Rates(Base):
    # Example
    #     "Cur_ID": 431,
    #     "Date": "2023-09-23T00:00:00",
    #     "Cur_Abbreviation": "USD",
    #     "Cur_Scale": 1,
    #     "Cur_Name": "Доллар США",
    #     "Cur_OfficialRate": 3.2590

    __tablename__ = "Rates"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    Cur_ID = Column("Cur_ID", Integer)
    Date = Column("Date", DateTime())
    Cur_Abbreviation = Column("Cur_Abbreviation", String(3))
    Cur_Name = Column("Cur_Name", String(50))
    Cur_Scale = Column("Cur_Scale", Integer)
    Cur_OfficialRate = Column("Cur_OfficialRate", Float)
