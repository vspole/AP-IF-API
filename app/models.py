from pydantic import BaseModel
from typing import Optional

class Group(BaseModel):
    groupID: Optional[int] = 0
    userID: Optional[int] = 0
    longitude: int
    latitude: int
    numberOfUsers: Optional[int] = 0
    numberDone: Optional[int] = 0
    creatorName: str

class User(BaseModel):
    groupID: int
    userID: Optional[int] = 0
    name: str
