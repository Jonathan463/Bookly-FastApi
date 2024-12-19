from fastapi import FastAPI, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


@app.get("/")
async def get_root():
    return {"message": "app running properly"}


@app.get("/greeting/{name}")
async def greeting(name:str) -> dict:
    return {"Message ": f" Hello {name}"}


@app.get("/greeting/")
async def greeting_query_parameter(name:str) -> dict:
    return {"Message ": f" Hello {name}"}


@app.get("/multiparameter/{name}")
async def greeting_multi_parameter(name:str, age:int) -> dict:
    return {"Message ": f" Hello my name is {name} and I am {age} years old "}


#Optional params
@app.get("/multiparameter/")
async def greeting_multi_parameter(name:Optional[str] = "User", age:int = 0) -> dict:
    return {"Message ": f" Hello my name is {name} and I am {age} years old "}

class BookModel(BaseModel):
    title : str
    author : str

@app.post("/create_book")
async def create_book(bookObject : BookModel):
    return {
        "title" : bookObject.title,
        "author" : bookObject.author
    }

@app.get('/get_headers')
async def get_headers(accept:str =Header(None), content_type:str = Header(None),
                      user_agent:str = Header(None), host : str = Header(None)):

    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host
