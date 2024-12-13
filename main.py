from fastapi import FastAPI

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