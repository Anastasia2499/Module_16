#uvicorn Module_16.mod_16_1:app
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def main() -> str:
    return f"Главная страница"

@app.get(('/user/admin'))
async def admin() -> str:
    return f'Вы вошли как администратор'

@app.get(('/user/{user_id}'))
async def user(user_id) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/id")
async def info(username: str, age: int) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

