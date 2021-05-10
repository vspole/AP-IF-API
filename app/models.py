from pydantic import BaseModel
from typing import Optional

class Group(BaseModel):
    groupID: Optional[str] = None
    longitude: int
    latitude: int
    numberOfUsers: Optional[int] = 1
    numberDone: Optional[int] = 0
    
