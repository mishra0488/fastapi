from typing import Optional
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time

app = FastAPI()

# we use pydent library to set the schema aur the format in which we wanr data from frontend
# like we want title str, and content str
# define a class for what a post should look like
class Post(BaseModel):
    title: str                # mandetory
    content: str              # mandetory
    published: bool = True    # optional


# We can create the schema for update as well(although it is same here, so not creating)
# class UpdatePost(BaseModel):
#     title: str                # mandetory
#     content: str              # mandetory   

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', 
        password='Mahadev#4321', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection was successfull")
        break
    except Exception as error:
        print("connection to database failed") 
        print("Error: ", error)  
        time.sleep(2) 


@app.get("/")
def root():
    return {"message": "Hello World"}


# getting all posts
@app.get("/posts")
def get_posts():
    cursor.execute("""select * from posts """)
    posts = cursor.fetchall()
    return {"data": posts}


# Creating posts
@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):   # here Post refer to class above pydentic model
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING * """, (post.title,
    post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()  # To save changes in database
    return {"data": new_post}


# getting single post
@app.get("/posts/{id}")
def get_post(id: int):
    cursor.execute("""SELECT * from posts WHERE id = %s """, (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post detail": post}


# deleting post
@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cursor.execute("""DELETE from posts WHERE id = %s RETURNING * """, (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Updating post
@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cursor.execute("""UPDATE posts SET title=%s, content=%s, published=%s WHERE id = %s RETURNING * """, (post.title,
    post.content, post.published, str(id),))
    updated_post = cursor.fetchone()
    conn.commit()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    return {"data": updated_post}    