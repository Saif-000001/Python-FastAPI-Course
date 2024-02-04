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

# Multiple Parameters
""" 
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

# Body - Fields
""" from typing import Annotated, Union
from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()

class Item(BaseModel):
    name:str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )

    price : float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.put("/items/{item_id}")
def update_item(item_id:int, item:Annotated[Item, Body(embed=True)]):
    result = {"item_id":item_id, "item": item}
    return result
 """


# Body - Nested Models
""" from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl

class Image(BaseModel):
    url:HttpUrl
    name:str

class Item(BaseModel):
    name: str
    description:Union[str, None] = None
    price: float
    tax:Union[str, None]=None
    tags: Union[List[Image], None] = None

class Offer(BaseModel):
    name: str
    description: Union[str, None] = None
    items: List[Item]

app = FastAPI()

# @app.put("/items/{item_id}")
# def update_item(item_id:int, item:Item):
#     results = {"item_id":item_id, "item":item}
#     return results

@app.post("/offers/")
def create_offer(offer:Offer):
    return offer
 """

# Extra Data Types
""" 
from datetime import datetime, time, timedelta
from typing import Annotated, Union
from uuid import UUID

from fastapi import FastAPI, Body

app = FastAPI()

@app.put("/items/{item_id}")
def update_item(
    item_id : int,
    start_datetime:Annotated[Union[datetime,None], Body()] = None,
    end_datetime: Annotated[Union[datetime, None], Body()] = None,
    reapet_at: Annotated[Union[time,None],Body()] = None,
    proces_after:Annotated[Union[timedelta, None], Body()] = None
):
    start_proces = start_datetime + proces_after
    duration = end_datetime - start_proces

    return{
        "item id": item_id,
        "start datetime": start_datetime,
        "end datetime": end_datetime,
        "reapet at":reapet_at,
        "proces after":proces_after,
        "start proces": start_proces,
        "duration": duration,
    }
 """

# Response Model - Return Type

""" # from typing import Any
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# class UserIN(BaseModel):
#     userName: str
#     password: str
#     email: EmailStr
#     fullName: str | None = None

# class UserOUT(BaseModel):
#     userName: str
#     email: EmailStr
#     fullName: str | None = None

# app = FastAPI()

# @app.post("/user/", response_model=UserOUT)
# def create_user(user:UserIN)->Any:
#     return user

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The Bar fighters", "price": 62, "tax": 20.2},
    "baz": {
        "name": "Baz",
        "description": "There goes my baz",
        "price": 50.2,
        "tax": 10.5,
    },
}


@app.get(
    "/items/{item_id}/name",
    response_model=Item
)
def read_item_name(item_id: str):
    return items[item_id]


@app.get("/items/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
def read_item_public_data(item_id: str):
    return items[item_id]

 """

# Extra Models
""" from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    description: str

app = FastAPI()

items = [
    {"name": "Foo", "description": "There comes my hero"},
    {"name": "Red", "description": "It's my aeroplane"},
]

@app.get('/items/', response_model=list[Item])
def read():
    return items """

# Response Status Code
# from typing import Union, Annotated
# from fastapi import FastAPI, status , Form
# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age : int
#     institute: Union[str, None] = None

# app = FastAPI()

# # @app.post("/users/{user_id}", status_code=status.HTTP_201_CREATED)
# # def create_user(user_id:int, user : User):
# #     result = {"user id": user_id, "user": user}
# #     return result

# @app.post("/login/", status_code=status.HTTP_201_CREATED)
# def login(userName: Annotated[str, Form()], password: Annotated[int, Form()]):
#     return {"userName" : userName}


# Request Files

""" 
from typing import Annotated

from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file} 
"""

