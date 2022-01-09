from typing import Optional
from pydantic import BaseModel, EmailStr
from pydantic.types import conint
from datetime import datetime

# Create a schema for how messages should be structured
# Set default value to make field optional


# class Post(BaseModel):
#     title: str
#     content: str
#     published: bool = True
#     # rating: Optional[int] = None

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class UserOut(BaseModel):
    id: int
    email: str
    created_at: datetime

    # converts model to dict
    class Config:
        orm_mode = True


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True


class PostOut(BaseModel):
    Post: Post
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
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
