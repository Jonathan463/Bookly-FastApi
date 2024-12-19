from fastapi import FastAPI
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
