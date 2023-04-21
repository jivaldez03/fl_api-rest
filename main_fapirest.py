"""
https://www.youtube.com/watch?v=J0y2tjBz2Ao

python3 -m venv fastapi_env

pip install fastapi

pip install uvicorn

// crear programa con función
//activar uvicorn

uvicorn main:app --reload
"""
from fastapi import HTTPException #, FastAPI
#from pydantic import BaseModel
#from typing import Optional

from app import create_app
from app.model.md_books import Book
from uuid import  uuid4 as uuid

app = create_app()


"""
class Book(BaseModel):
    title: str
    author: str
    pages: int
    editorial: Optional[str]
"""

@app.get("/")
def index():
    return "hello pythonician"

@app.get("/hello")
def helloworld():
    return {'message': "hello world"}

@app.get("/books/author/{id_book} {id_sin}")
def book_author(id_book:int, id_sin):
    if id_sin == None:
        id_sin = 'n/a'
    elif id_sin == '....':
        pass
    else:
        raise HTTPException(status_code=404, detail="record not foundS")

    return {'id': id_book
            ,'author': 'Jorge Iduvas'
            , 'sin_code': id_sin
            }

@app.post("/books/new_book/")
def new_book(book: Book):
    return {'message': f"{book.title} insertado"
            }

#resp = make_response(redirect('http://127.0.0.1:8000/hello'))
#print(resp)


