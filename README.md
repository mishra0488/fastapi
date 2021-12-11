# To start the server
````
uvicorn app.main:app
````
# below  cmd if  ot want to restart the server after every change
````
uvicorn app.main:app --reload
````
````
uvicorn app.mainORM:app --reload
````

# making connection with database postgress without ORM
https://www.psycopg.org/docs/

# with ORM i.e. sqlalchemy
````
pip install sqlalchemy
````

# for hashing of password
````
pip install passlib[bcrypt]
````

# for authhentication
````
pip install python-jose[cryptography]
````

# to over come the weekness of sqlalchemy(can not add the column), we use alambic
````
pip install alembic
````
# to create a folder alembic
````
alembic init alembic
````
# after this we need to import base from database to alembic env file
# and in .ini file update sqlalchemyurl path

# CORS(cross origin resource sharing) allows to make requests from a web browser on one domain to a server on diff domain
# by default our APi will only allow web browser running on same domainas our server to make request to it.

# to include all the already downloaded packages in requirements.txt
````
pip freeze > requirements.txt
````
# after that if anyone wants to install all packages, just run requirements.txt
````
pip install -r requirements.txt
````