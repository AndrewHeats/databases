
from __future__ import annotations

from datetime import date
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto
route_passenger = db.Table(
    'route_passenger',
    db.Column('route_id', db.Integer, db.ForeignKey('route.id')),
    db.Column('passenger_id', db.Integer, db.ForeignKey('passenger.id'))
)

class Passenger(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "passenger"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(40))
    surname: str = db.Column(db.String(40))
    date_of_birth: date = db.Column(db.Date)
    phone_number: str = db.Column(db.String(13))
    routes = db.relationship('Route', secondary=route_passenger, backref=db.backref('routes', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Passenger({self.id}, {self.name}, {self.surname}, {self.date_of_birth}, {self.phone_number})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "date_of_birth": self.date_of_birth,
            "phone_number": self.phone_number,
            "routes": [route.put_into_dto() for route in self.routes],
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Passenger:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Passenger(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            date_of_birth=dto_dict.get("date_of_birth"),
            phone_number=dto_dict.get("phone_number")
        )
        return obj
