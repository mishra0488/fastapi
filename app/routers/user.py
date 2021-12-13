from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, utils
from ..schemas import Post, CreatePost, UpdatePost, PostResponse, CreateUser, UserOut
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional


router = APIRouter(
    prefix= "/users",
    tags=['Users']
)


#create user
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


#get user
@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
    return user


#get all user
@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db), search: Optional[str] = ""):
    users = db.query(models.User).filter(models.User.email.contains(search)).all()
    
    return users