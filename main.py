from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main_page() -> dict:
    return{'message': "Главная страница"}

@app.get('/user/admin')
async def admin_page() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/{user_id}')
async def user_page(user_id):
    return {'message': f'Вы вошли как пользователь №{user_id}'}

@app.get('/user')
async def user_info(username:str = 'SomeOne', age: int = 666):
    return {'Информация о пользователе:': f'Имя: {username} Возраст: {age}'}
    
    