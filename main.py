
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, GitHub World!"}

@app.get("/square/{number}")
def square_number(number: int):
    return {"number": number, "square": number ** 2}


@app.get("/cube/{number}")
def cube_number(number: int):
    return {"number": number, "cube": number ** 3}
