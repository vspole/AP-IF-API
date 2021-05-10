from pydantic import BaseModel
from typing import Optional

class Group(BaseModel):
    groupID: Optional[int] = 0
    userID: Optional[int] = 0
    longitude: float
    latitude: float
    radius: int
    creatorName: str

class User(BaseModel):
    groupID: int
    userID: Optional[int] = 0
    name: str

class Restaurant(BaseModel):
    name: str
    priceLevel: Optional[int] = 0
    rating: Optional[int] = 0
