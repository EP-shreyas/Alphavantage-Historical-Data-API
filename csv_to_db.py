from datetime import datetime
import pandas as pd
from database import engine
def add_to_mst():
    df = pd.read_csv("listing_status.csv")
    df.drop(['delistingDate','status'],axis=1,inplace=True)
    print(df.columns)
    # LIST=["AA","ABNB","ADBE","ADI","ADP","ADSK","AEP","ALGN","AMAT","AMD","AMGN","AMZN","ANSS","ASML","ATVI","AVGO","AZN","BIDU","BIIB","BKNG","CDNS","CEG","CHTR","CMCSA","COST","CPRY","CEWD","CSCO","CSX","CTAS","CTSH","DDOG","DLTR","DOCU","DXCM","EA","EBAY","EXC","FAST","FB","FISV","FTNT","GILD","GOOG","GOOGL","HON","IDXX","ILMN","INTC","INTU","ISRG","JD","KDP","KHC","KLAC","LCID","LRCX","LULU","MAR","MCHP","MDLZ","MELI","MNST","MRNA","MRVL","MSFT","MTCH","MU","NFLX","NTES","NVDA","NXPI","ODFL","OKTA","ORLY","PANW","PAYX","PCAR","PDD","PEP","PYPL","QCOM","REGN","ROST","SBUX","SGEN","SIRI","SNPS","SPLK","SWKS","TEAM","TMUS","TSLA","TXN","VRSK","VRSN","VRTX","WBA","WDAY","XEL","ZM","ZS"]
    LIST= ['AAPL',"GOOG","GOOGL","MSFT","TSLA"]
    df = df[df['symbol'].isin(LIST)]
    df.rename(columns={'symbol':'ticker_name',"name":"company_name","exchange":"exchange_name","assetType":"asset_type","ipoDate":"ipo_date"},inplace=True)
    df['ipo_date']=pd.to_datetime(df['ipo_date'],format='%Y-%m-%d')
    df['application_id']=1
    df['bu_id']=1
    df['sub_bu_id']=1
    df['is_active']=True
    df['created_by']=1
    df['created_date']=datetime.now()
    df['last_modified_by']=1
    df['last_modified_date']=datetime.now()
    print(df.dtypes)
    df.to_sql('mst_stock_detail', engine, if_exists='replace', index=False)