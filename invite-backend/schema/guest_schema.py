from pydantic import BaseModel


class GuestCreate(BaseModel):
    name: str
    place: str
    message: str

class GuestResponse(BaseModel):
    id: int
    name: str
    place: str
    message: str
