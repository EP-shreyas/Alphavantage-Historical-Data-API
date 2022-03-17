import time
from fastapi import FastAPI,status
import sqlalchemy

import json
from fastapi.responses import JSONResponse

import models
from csv_to_db import add_to_mst
from database import engine, SessionLocal
from schemas import Stock, Hist_details, Ticker
from test import get_data
from producer import prod,prod_2
from consumer import cons,cons_2
from utils import jsonresponse, payloadCheckGetHistData, payloadCheckHistData


models.Base.metadata.create_all(bind=engine)


app = FastAPI()

@app.get('/chk_mst')
def check_master():
    conn = engine.connect()
    md = sqlalchemy.MetaData()
    master = sqlalchemy.Table('mst_stock_detail', md, autoload=True, autoload_with=engine)
    query = sqlalchemy.select([master])
    result = conn.execute(query).fetchall()
    if len(result)==0:
        return {"Empty table"}
    else:
        return {"Master Table present"}

@app.post('/add_to_mst')
def add():
    add_to_mst()
    return {"Data added to Master"}


@app.get('/')
def index():
    return{'data':'stock'}

@app.post('/posthistorical')
def post_historical(stock:Stock):
    result=payloadCheckHistData(stock)
    # print(result.status_code)
    if result.status_code==status.HTTP_400_BAD_REQUEST:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','Invalid data','','',''))
    conn = engine.connect()    
    md = sqlalchemy.MetaData()
    master = sqlalchemy.Table('mst_stock_detail', md, autoload=True, autoload_with=engine)
    query = sqlalchemy.select([master])
    result = conn.execute(query).fetchall()
    if len(result)==0:
        return {"Empty Master table"}
    # tickers_data = []
    for i in range(len(result)):
        if i!=0 and i%5==0:
           time.sleep(60)
        df = get_data(result[i].ticker_name)
        # print()
        df['stock_name_id']=result[i].stock_detail_id
        # print(df)
        
        # print("result",result)
        my_dict = {"ticker":result[i].ticker_name,"time":str(df.historical_price_date_time[0]),"open":df.day_open_price[0],"close":df.day_close_price[0],"high":df.day_high_price[0],"low":df.day_low_price[0],"volume":df.day_volume[0]}
        df_json = json.dumps(my_dict,indent=4)
        prod(df_json)
        cons()
        df.to_sql('txn_stock_price_historical', engine, if_exists='append', index=False)
        # print(tickers_data)
    return("data added")

@app.post('/getHistoricalData',response_model=Hist_details)
def get_historical(ticker:Ticker):
    result = payloadCheckGetHistData(ticker)
    # print("result=",result)
    if result.status_code==status.HTTP_400_BAD_REQUEST:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','Invalid data','','',''))
    db = SessionLocal()
    ticker = (ticker.name).upper()
    mst_stock = db.query(models.Master).filter(models.Master.ticker_name==ticker)
    res_1 = mst_stock.first()
    if res_1==None:
        return Hist_details(response=404)
    hist_stock = db.query(models.Stock).filter(models.Stock.stock_name_id==res_1.stock_detail_id)
    res_2 = hist_stock.first()
    my_dict = {"ticker":ticker,"company":res_1.company_name,"open":res_2.day_open_price,"close":res_2.day_close_price,"high":res_2.day_high_price,"low":res_2.day_low_price,"volume":res_2.day_volume}
    df_json = json.dumps(my_dict,indent=4)
    prod_2(df_json)
    cons_2()
    return Hist_details(response = 200,ticker=ticker,company=res_1.company_name,day_open=res_2.day_open_price,day_close=res_2.day_close_price,day_high=res_2.day_high_price,day_low=res_2.day_low_price,day_volume=res_2.day_volume)
