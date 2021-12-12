from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, oauth2
from ..schemas import Post, CreatePost, PostOut, UpdatePost, PostResponse
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from ..database import get_db
from .. import schemas


router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# getting all posts
@router.get("/", response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # if you want to show only users posts and not others posts to user , then use below line
    #posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()

    # below query to show vote counts in response for perticular posts
    # left join query to join the tables and counts the votes on posts
    posts = db.query(models.Post, func.count(models.Vote.post_id).label("likes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    return posts


# Creating posts
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
def create_posts(post: CreatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    print(current_user.email)
    new_post = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# getting single post
@router.get("/{id}", response_model=PostOut)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    #post = db.query(models.Post).filter(models.Post.id == id).first()
    
    # below query to show vote counts in response for perticular posts
    # left join query to join the tables and counts the votes on posts
    post = db.query(models.Post, func.count(models.Vote.post_id).label("likes")).join(
        models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    
    # if you want to show only users posts and not others posts to user , then use below line
    # if post.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")    
    return post


# deleting post
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    query = db.query(models.Post).filter(models.Post.id == id)
    post = query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    # to delete their own post and not others
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


# Updating post
@router.put("/{id}", response_model=PostResponse)
def update_post(id: int, updated_post: UpdatePost, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")

    # to update their own post and not oters
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first() 