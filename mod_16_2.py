#uvicorn Module_16.mod_16_2:app
from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def main() -> str:
    return f"Главная страница"

@app.get(('/user/admin'))
async def admin() -> str:
    return f'Вы вошли как администратор'

@app.get(('/user/{user_id}'))
async def user(user_id: int = Path(ge=1, le=100, description='Enter User ID', example="1")) -> str:
    return f'Вы вошли как пользователь № {user_id}'

@app.get("/user/{username}/{age}")
async def info(username: str = Path(min_length=5, max_length=20, description="Enter username", example='UrbanUser')
               , age: int = Path(ge=18, le=120, description='Enter age', example="24")) -> str:
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'