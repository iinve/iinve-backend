from sqlalchemy import Column, Integer, String

from database.db import Base


class Guest(Base):
    __tablename__ = "guests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    place = Column(String, index=True)
    message = Column(String)

