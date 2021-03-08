from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Float

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    sell_price = Column(Float)
    buy_price = Column(Float)

    def __repr__(self):
        return '{0} - Buy = {1}, Sell = {2} ({3})'.format(self.id, self.buy_price, self.sell_price, self.date)