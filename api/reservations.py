from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import get_db
from models import Reservation
from datetime import datetime

router = APIRouter()


class ReservationCreate(BaseModel):
    name: str
    phone_number: str
    number_of_people: int
    reservation_time: datetime


@router.post("/reserve")
def reserve_table(reservation: ReservationCreate, db: Session = Depends(get_db)):
    reservation_data = reservation.dict()
    db_reservation = Reservation(**reservation_data)
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return {"message": "Reservation made successfully", "reservation_id": db_reservation.id}

