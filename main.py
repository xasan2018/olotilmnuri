from fastapi import FastAPI
from schemas import Book
import cv2

app = FastAPI()

def rasm(path):
    img = cv2.imread(path)
    soni=img.shape
    return soni

img="1.jpg"

rasmlar=rasm(img)


@app.get('/')
def home():
    xat=rasmlar
    return {"key":xat}


@app.get('/{pk}')
def get_item(pk: int,q: int = None):
    return {"key": pk,"q": q}

@app.get('/parol/{pk}/soni/{ball}/')
def get_user_item(pk: int,ball: int):
    return {"parol": pk,"ball": ball}

@app.post('/book')
def create_book(item: Book):
    return item