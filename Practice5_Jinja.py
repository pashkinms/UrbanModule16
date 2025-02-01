from fastapi import FastAPI, Request, Path, HTTPException
from fastapi.responses import HTMLResponse
from typing import Annotated, List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

app = FastAPI(swagger_ui_parameters={'tryItOutEnabled': True}, debug=True)

templates = Jinja2Templates(directory="templates")

users = []

class User(BaseModel):
    id: int 
    username: str
    age: int

@app.get('/', response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse('users.html',{'request': request, 'users': users})

@app.get('/user/{user_id}', response_class= HTMLResponse)
async def get_user(request: Request, user_id: Annotated[int, Path(ge=1)]):
    for user in users:
        if user.id == user_id:
            return templates.TemplateResponse('users.html',{'request': request, 'user': user})


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