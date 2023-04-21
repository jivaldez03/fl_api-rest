"""
https://www.youtube.com/watch?v=J0y2tjBz2Ao

python3 -m venv fastapi_env

pip install fastapi

pip install uvicorn

// crear programa con función
//activar uvicorn

uvicorn main:app --reload --host 
uvicorn main_fapirest:app --reload --host localhost --port 3000
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
    return "Hello EVERYBODY ..... dELTA-pHASE is now working for you"

@app.get("/hello")
def helloworld():
    return {'message': "hello world"}

@app.get("/get_/categories/{user_id}")
def get_categories_subc(user_id):
    listcat = [{ 'category': 'Anathomy'
                        , 'idCat': 'cat.01.01'
                        , 'subcategories' : [
                            {'subcategory': 'human body' , 'idSCat': 'scat.01.01'}
                            , {'subcategory': 'human skeleton' , 'idSCat': 'scat.01.02'}
                            , {'subcategory': '_alls' , 'idSCat': 'scat.01.00'}
                        ]
                }
                , {'category': 'Animals'
                        , 'idCat': 'cat.01.02'
                        , 'subcategories' : [
                            {'subcategory': 'aquatics' , 'idSCat': 'scat.03.01'}
                            , {'subcategory': 'amphibians' , 'idSCat': 'scat.03.02'}
                            , {'subcategory': 'mamals' , 'idSCat': 'scat.03.03'}
                            , {'subcategory': '_alls' , 'idSCat': 'scat.03.00'}
                        ]        
                }, {'category': 'Music'
                        , 'idCat': 'cat.01.04'
                        , 'subcategories' : [
                            {'subcategory': 'Instruments' , 'idSCat': 'scat.04.01'}
                            , {'subcategory': 'Famous Classical Compositors' , 'idSCat': 'scat.04.02'}
                            , {'subcategory': 'Famous Jazz Musician' , 'idSCat': 'scat.04.03'}
                            , {'subcategory': '_alls' , 'idSCat': 'scat.04.00'}
                        ]        
                }, {'category': 'Geography'
                        , 'idCat': 'cat.01.05'
                        , 'subcategories' : [
                            {'subcategory': 'Mountains' , 'idSCat': 'scat.05.01'}
                            , {'subcategory': 'Rivers' , 'idSCat': 'scat.05.02'}
                            , {'subcategory': 'Continents/Oceans/Gulfs' , 'idSCat': 'scat.05.03'}
                            , {'subcategory': 'Countries/Capitals' , 'idSCat': 'scat.05.03'}
                            , {'subcategory': '_alls' , 'idSCat': 'scat.05.00'}
                        ]        
                }
               ]
    return {'message': listcat}


@app.get("/books/author/{id_book} {id_sin}")
def book_author(id_book:int, id_sin):
    if id_sin == None:
        id_sin = 'n/a'
    elif id_sin != '....':
        pass
    else:
        raise HTTPException(status_code=404, detail="record not found")

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


#if __name__ == "__main__":
#	app.run(host='0.0.0.0', port=3000, debug=True)
