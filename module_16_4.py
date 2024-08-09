from fastapi import FastAPI, Body, status, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/users')
async def get_dict() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_info(user: User, username: str, age: int) -> User:
    if not users:
        user.id = 1
    else:
        user.id = len(users) + 1
    user.username = username
    user.age = age
    users.append(user)
    return user


@app.put('/user/{id}/{username}/{age}')
async def update_info(id: int, username: str, age: int) -> User:
    for i in users:
        if i.id == id:
            i.username = username
            i.age = age
            return i
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{id}')
async def delete_info(id: int) -> User:
    for i in users:
        if i.id == id:
            users.remove(i)
            return i
    raise HTTPException(status_code=404, detail="User was not found")