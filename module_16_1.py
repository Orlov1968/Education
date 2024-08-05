from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def entrance() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def string_of_admin() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def string_of_user(user_id: int) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/id")
async def about_user(username: str, age: int) -> str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
