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


