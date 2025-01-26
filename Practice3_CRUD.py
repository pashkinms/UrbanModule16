from fastapi import FastAPI
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_all_users() -> dict:
    return users

@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> str:
    user_id = str(len(users) + 1)
    users.update({user_id : f'Имя: {username}, возраст: {age}'})
    return f'User {user_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: str) -> str:
    users[str(user_id)] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(user_id) -> str:
    users.pop(str(user_id))
    return f'User {user_id} is deleted'