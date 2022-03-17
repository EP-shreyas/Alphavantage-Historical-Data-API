from typing import Optional
from pydantic import BaseModel

class Stock(BaseModel):
    tool_type:int
    
class Ticker(BaseModel):
    name:str

class Hist_details(BaseModel):
    response:int
    ticker:Optional[str]
    company:Optional[str]
    day_open:Optional[float]
    day_high:Optional[float]
    day_low:Optional[float]
    day_close:Optional[float]
    day_volume:Optional[float]
    