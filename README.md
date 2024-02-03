# Python-FastAPI-Course

--------------- 01-02-2024 ----------------

#--------------Feature of Fast API-----------------

01. Authentication -----> HTTPS
02. CRUD Operation ----->  Create, Read, Update, and Delete
03. Validation     -----> Query Parameters and String
04. Documentation 

#---------------> Deployment
01. Ubuntu
02. Heroku
03. Docker
04. CI/CD
# FastApi
# SQLAlchemy


# FastApi
install -> pip install "fastapi[all]"
-> pip freeze 
 
# Create and activate the virtual environment:
install ---> python3 -m venv venv
---> source venv/bin/activate

# FastApi Run 
-> uvicorn main:app --reload

--------------------------02-02-2024-------------------
# create a path operation
# HTTP Methods 
<!--    POST: to create data.
        GET: to read data.
        PUT: to update data.
        DELETE: to delete data 

        # More exotic ones
           # OPTIONS
           # HEAD
           # PATCH
           # TRACE
-->

# path operation function
<!-- 
       # path: is /.
       # operation: is get.
       # function: is the function below the "decorator" (below @app.get("/"))

       Example: @app.get("/")
 -->

# Recap
<!-- 
    Import FastAPI.
    Create an app instance.
    Write a path operation decorator (like @app.get("/")).
    Write a path operation function (like def root(): ... above).
    Run the development server (like uvicorn main:app --reload). 
-->

# You can only use await inside of functions created with async def.

# Order matters
<!-- if tow function is same pathe, fist function always show in documentation  -->


# Create an Enum class
<!-- 
        Enumerations in Python are implemented by using the module named “enum“. Enumerations are created using classes. Enums have names and values associated with them 
-->

--------------------03-02-2024--------------
# Query Parameters
<!-- 
When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
 -->

<!-- The query is the set of key-value pairs that go after the ? in a URL, separated by & characters. -->

# there are 3 query parameters:
<!-- 
       1. needy, a required str.
       2. skip, an int with a default value of 0.
       3. limit, an optional int.
-->

# Request Body
<!--To declare a request body, I use Pydantic models with all their power and   benefits. 
-->

<!-- 
        To send data, you should use one of: POST (the more common), PUT, DELETE or PATCH.
 -->

 # First, you need to import BaseModel from pydantic

 # Pydantic
 <!-- Dataclasses, TypedDicts -->

 <!-- 
 Pydantic provides four ways to create schemas and perform validation and serialization:

       01. BaseModel — Pydantic's own super class with many common utilities available via instance methods.

       02. pydantic.dataclasses.dataclass — a wrapper around standard dataclasses which performs validation when a dataclass is initialized.

       03. TypeAdapter — a general way to adapt any type for validation and serialization. This allows types like TypedDict and NampedTuple to be validated as well as simple scalar values like int or timedelta — all types supported can be used with TypeAdapter.

       04. validate_call — a decorator to perform validation when calling a function. 
        -->
        
<!-- FastAPI will know that the value of q is not required because of the default  value = None.
 -->