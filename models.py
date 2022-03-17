from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Float,Boolean

from database import Base


class Stock(Base):
    __tablename__ = 'txn_stock_price_historical'
    stock_price_historical_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer)
    bu_id = Column(Integer)
    sub_bu_id = Column(Integer)
    stock_name_id = Column(Integer, ForeignKey('mst_stock_detail.stock_detail_id'))
    historical_price_date_time = Column(String)
    tool_type = Column(Integer)
    day_open_price=Column(String)
    day_high_price = Column(String)
    day_low_price = Column(String)
    day_close_price = Column(String)
    day_volume = Column(String)
    is_active = Column(Boolean)
    created_by = Column(Integer)
    created_date = Column(DateTime)
    last_modified_by = Column(Integer)
    last_modified_date = Column(DateTime)

class Master(Base):
    __tablename__ = "mst_stock_detail"
    stock_detail_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer)
    bu_id = Column(Integer)
    sub_bu_id = Column(Integer)
    ticker_name = Column(String)
    company_name = Column(String)
    company_description = Column(String)
    exchange_name = Column(String)
    asset_type = Column(String)
    ipo_date = Column(String)
    is_active = Column(Boolean)
    created_by = Column(Integer)
    created_date = Column(DateTime)
    last_modified_by = Column(Integer)
    last_modified_date = Column(DateTime)
