from fastapi.responses import JSONResponse
from fastapi import status

def jsonresponse(reasonCode,status,reasonText,responseObject,totalRecords,responseListObject):
    json={
        "reasonCode":reasonCode,
        "status":status,
        "reasonText":reasonText,
        "responseObject":responseObject,
        "totalRecords":totalRecords,
        "responseListObject":responseListObject
    }
    return json

def payloadCheckHistData(stock):
    tt = stock.tool_type
    if tt ==" " or tt==0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','Invalid data','','',''))
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("200","success","Payload Valid","","",""))

def payloadCheckGetHistData(ticker):
    t_name = ticker.name
    if t_name ==" " or t_name==None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content= jsonresponse('400','fail','Invalid data','','',''))
    return JSONResponse(status_code=status.HTTP_200_OK,content=jsonresponse("200","success","Payload Valid","","",""))