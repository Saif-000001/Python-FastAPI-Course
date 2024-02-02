from fastapi import FastAPI
from enum import Enum

# class ModelName(str, Enum):
#     pujaCherry = 'pujaCherry'
#     prarthanaFardinDighi = 'prarthanaFardinDighi'
#     purnima = 'purnima'
#     shabnur = "shabnur"

app = FastAPI()

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



    

@app.get('/')
def read():
    return {"message": "Hello World"}

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




