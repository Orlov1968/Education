from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int = None


@app.get('/')
async def get_all_dict(request: Request, ) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{id}')
async def get_dict(request: Request, id: int) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "user": users[id - 1]})


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
