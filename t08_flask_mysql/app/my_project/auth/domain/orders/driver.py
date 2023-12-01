# driver.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

driver_bus = db.Table(
    'driver_bus',
    db.Column('driver_id', db.Integer, db.ForeignKey('driver.id')),
    db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
    extend_existing=True
)


class Driver(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "driver"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name: str = db.Column(db.String(12))
    surname: str = db.Column(db.String(20))
    company: str = db.Column(db.String(40))

    # Many-to-Many relationship with Bus
    buses = db.relationship('Bus', secondary=driver_bus, backref=db.backref('drivers_associated', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Driver({self.id}, {self.name}, {self.surname}, {self.company})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "company": self.company,
        }


    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Driver:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Driver(
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            company=dto_dict.get("company")
        )
        return obj
