from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


# @app.get("/")
# async def entrance() -> str:
#     return "Главная страница"


# @app.get("/user/admin")
# async def string_of_admin() -> str:
#     return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def string_of_user(user_id: int = Path(ge=1, le=100, description="Enter User ID", examples=4)) -> str:
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/{age}")
async def about_user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                                   examples="Urban User")],
                     age: Annotated[int, Path(ge=18, le=120, description="Enter age", examples=37)]):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"
