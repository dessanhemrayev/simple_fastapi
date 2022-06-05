# import uvicorn
from fastapi import FastAPI
from operations import get_user,get_all_users,create_user,create_lpressure,create_hpressure,create_heatbeatrate

from typing import Union
from pydantic import BaseModel


class User(BaseModel):
    nickname: str
    telegram_id: Union[str, None] = None
    phone: Union[str, None] = None
   

class High(BaseModel):
    user_id: str
    value: str

class Low(BaseModel):
    user_id: str
    value: str  

class Rate(BaseModel):
    user_id: str
    value: str   

app = FastAPI()
@app.get("/")
def all_users():
    return get_all_users()

@app.get("/user/{user_id}")
def getUserInfo(user_id: int):
    return get_user(user_id)

@app.post("/user/create")
def createUser(user: User):
    data={}
    data['nickname']= user.nickname
    data['telegram_id']= user.telegram_id
    data['phone']= user.phone
    create_user(data)
    return get_all_users()

@app.post("/user/hpressure/create")
def createHigh(high: High):
    data={}
    data['user_id']= high.user_id
    data['value']= high.value
    create_hpressure(data)
    
    return {'message':'succes'}

@app.post("/user/lpressure/create")
def createLow(low: Low):
    data={}
    data['user_id']= low.user_id
    data['value']= low.value
    create_lpressure(data)
    
    return {'message':'succes'}

@app.post("/user/rate/create")
def createRate(rate: Rate):
    data={}
    data['user_id']= rate.user_id
    data['value']= rate.value
    create_lpressure(data)
    
    return {'message':'succes'}
# if __name__ == "__main__":
#     uvicorn.run(app, host="84.252.75.168", port=8001)

    