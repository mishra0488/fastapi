from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint


# For requests
class Post(BaseModel):
    title: str                # mandetory
    content: str              # mandetory
    published: bool = True    # optional


class CreatePost(Post): # inherited above post
    pass


class UpdatePost(Post): # inherited above post
    pass 


class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True


# for response
class PostResponse(Post): # inherating title content and published field already
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(Post):
    Post: PostResponse
    votes: int

    class Config:
        orm_mode = True

# --------------------------------------------------------------------------------------------------

class CreateUser(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)    