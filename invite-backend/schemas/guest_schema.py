from pydantic import BaseModel
from typing import Optional


class GuestBase(BaseModel):
    name: Optional[str] = None
    place: Optional[str] = None
    message: Optional[str] = None

class GuestCreate(GuestBase):
    name: str
    place: str
    message: str

class GuestUpdate(GuestBase):
    pass

class GuestResponse(BaseModel):
    id: int
    name: str
    place: str
    message: str

    class Config:
        from_attributes = True
