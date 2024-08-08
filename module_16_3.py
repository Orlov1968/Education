from fastapi import FastAPI

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_dict() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_info(username: str, age: int) -> str:
    new_index_key = str(int(max(users, key=int)) + 1)
    users[new_index_key] = f"Имя: {username} Возраст: {age}"
    return f"User {new_index_key} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_info(user_id: str, username: str, age: int) -> str:
    users[user_id] = f"Имя: {username} Возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete('/user/{user_id}')
async def delete_info(user_id: str) -> str:
    users.pop(user_id)
    return f"User {user_id} has been deleted"
