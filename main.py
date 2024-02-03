# from fastapi import FastAPI
# from enum import Enum

# class ModelName(str, Enum):
#     pujaCherry = 'pujaCherry'
#     prarthanaFardinDighi = 'prarthanaFardinDighi'
#     purnima = 'purnima'
#     shabnur = "shabnur"

# app = FastAPI()

""" 
@app.get('/models/{model_name}')
def select_model(model_name:ModelName):
    if model_name == 'pujaCherry':
        return f"{model_name} is very young model"
    elif model_name == 'prarthanaFardinDighi':
        return f"{model_name} is look like good"
    elif model_name == 'purnima':
        return f"{model_name} is crush of every generation"
    else:
        return f"{model_name} is just selected model" 
"""

# @app.get('/models/{model_name}')
# def get_model(model_name:ModelName):
#     if model_name is ModelName.prarthanaFardinDighi:
#         return f"{model_name} is good look model"
#     elif model_name == ModelName.pujaCherry:
#         return f"{model_name} is very young model"
    
#     return f"{model_name} is old model"



    

""" @app.get('/')
def read():
    return {"message": "Hello World"} """

# Path parameters with types
""" 
@app.get('/iteams/{iteams_id}')
def get_read(iteams_id:int):
    return{'id': iteams_id} 
"""


# Order matters
""" 
@app.get('/iteams/me')
def get():
    return{'name': 'MSI'}

@app.get('/iteams/me')
def get_hello():
    return{'name': 'SAIF'} 
"""

# Predefined values


# Query Parameters
# http://127.0.0.1:8000/items/
# http://127.0.0.1:8000/items/?skip=0&limit=10

""" fake_db = [{'iteam_name': 'keyboard'}, {'iteam_name':'mouse'}, {'iteam_name':'monitor'}]
@app.get('/items')
def check_quaryParameters(skip: int = 0, limit: int= 10):
    return fake_db[skip: skip+limit] """

# Required query parameters
# http://127.0.0.1:8000/items/mouse?price=500
""" @app.get('/items/{items_id}')
def requiredQueryParameters(items_id : str, price : int):
    items = {'items_id': items_id, 'price': price}
    return items """

""" # Request Body
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    name : str
    age : int | None = None
    device : str 
    price : int
    tax :float

app = FastAPI()

@app.get('/')
def show():
    return f"Welcome to my site "

@app.post('/users')
def create_data(user:User):
    user_dict = user.dict()
    if user.tax:
        price_with_tax = user.tax + user.price
        user_dict.update({'price_with_tax': price_with_tax})
    return user_dict

@app.put('/users/{user_id}')
def update_data(user_id: int, user:User):
    return {'user_id':user_id, **user.dict()} 

# Request body + path + query parameters
@app.put('/users/{user_id}')
def update_data(user_id:int, user:User, p:str | None = None):
    result = {"user_id":user_id, **user.dict()}
    if p:
        result.update({'p': p})
    return result
 """

# Query Parameters and String Validations

""" from typing import Annotated, Union
from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
# def read_item(q: Annotated[str | None, Query(max_length=50)]=None):
# def read_item(q: str | None = Query(default=None,max_length=50)):
# def read_items(
#    q: Annotated[str|None, Query(min_length=3, max_length=50, pattern="^fixdeqeue$")
#    ]=None
# ):
# def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
#     result ={ "items": [{"item_id":"foo"}, {"item_id":"bar"}]}
#     if q:
#         result.update({"q":q})
#     return result

# def read_item(q: Annotated[Union[list[str], None], Query()]=None):
#     query_item = {"q":q}
#     return query_item

def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results """


# Path Parameters and Numeric Validations

""" # Declare metadata
from typing import Annotated, Union
from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items/{item_id}')
# def read_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get")],
#     q: Annotated[str | None, Query(alias="Item-quary")] = None,
# ):

def read_item(
    q:str, item_id : Annotated[int , Path(title="The ID of the item to get", ge=0, le = 1000)]
):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    return result """

""" # Multiple Parameters
from typing import Annotated, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description:Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    userName: str
    fullName: Union[str, None] = None

app = FastAPI()

@app.put("\items\{item_id}")
def update_item(item_id:int, item:Item, user:User, importance: Annotated[int, Body()]):
    results = {"item_id":item_id, "item":item, "user":user, "importance":importance}
    return results """