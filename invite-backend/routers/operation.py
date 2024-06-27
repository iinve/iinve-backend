from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models.guest_model import Guest
from schemas.guest_schema import GuestCreate, GuestUpdate, GuestResponse
from database.db import get_db


router = APIRouter(
    prefix="/v1",
    tags=['Guests']
)


@router.post("/guests/", response_model=GuestResponse)
def create_guest(guest: GuestCreate, db: Session = Depends(get_db)):
    db_guest = Guest(name=guest.name, place=guest.place, message=guest.message)
    db.add(db_guest)
    db.commit()
    db.refresh(db_guest)
    return db_guest

@router.get("/guests/", response_model=List[GuestResponse])
def read_guests(skip: int = 0, limit: int = None, db: Session = Depends(get_db)):
    guests = db.query(Guest).offset(skip).limit(limit).all()
    return guests

@router.delete("/guests/{guest_id}", response_model=GuestResponse)
def delete_guest(guest_id: int, db: Session = Depends(get_db)):
    db_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    db.delete(db_guest)
    db.commit()
    
    return db_guest

@router.put("/guests/{guest_id}", response_model=GuestResponse)
def update_guest(guest_id: int, guest_update: GuestUpdate, db: Session = Depends(get_db)):
    db_guest = db.query(Guest).filter(Guest.id == guest_id).first()
    if not db_guest:
        raise HTTPException(status_code=404, detail="Guest not found")
    
    if guest_update.name is not None:
        db_guest.name = guest_update.name
    if guest_update.place is not None:
        db_guest.place = guest_update.place
    if guest_update.message is not None:
        db_guest.message = guest_update.message
    
    db.commit()
    db.refresh(db_guest)
    
    return db_guest
