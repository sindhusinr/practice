from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

class items(BaseModel):
    name:str =Field(min_length=3,max_length=50,pattern="[^a-zA-Z]")
    price:float =Field(gt=0,lt=1000000000000000)
    availability:Optional[bool] = None

app = FastAPI()
@app.post("/display/")
def view(data:items):
    return {"meesage":"item received","data":data}
