from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int 
    username: str
    age: int

@app.get('/users', response_model=List[User])
async def get_all_users() -> list:
    return users

@app.post('/user/{username}/{age}', response_model=User)
async def add_user(username: str, age: int):
    if len(users) == 0:
        new_id = 1
    else:
        new_id = users[-1].id +1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put('/user/{user_id}/{username}/{age}', response_model=User)
async def update_user(user_id: int, username: str, age: str):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}', response_model=User)
async def delete_user(user_id):
    for user in users:
        if user.id == int(user_id):
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail='User was not found')