from typing import Union

from fastapi import FastAPI #, Query, Path (import que se dejaron de utilizar)

# ruta de carpetas item y product
from models.item_model import Item

# from models.product import Product (imports que se dejaron utilizar)

# importacion del router que se creo
from routers.product import router as product_router

# creacionde de la app
app = FastAPI()

# nuetra aplicacion va inclueir un router
app.include_router(product_router)


# rutas creadas

@app.get("/")
def read_root():
    return {"Hello": "World!!!!"}

@app.get("/hola")
def hola_mundo():
    return {"Hola": "Mundo"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/calculadora")
def calcular(operador_1: float, operador_2: float):
    return {"suma": operador_1 + operador_2 }

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id,"item_price": item.price}

