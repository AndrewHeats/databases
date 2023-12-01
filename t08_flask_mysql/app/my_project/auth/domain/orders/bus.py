# bus.py
from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

bus_driver = db.Table(
    'driver_bus',
    db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
    db.Column('driver_id', db.Integer, db.ForeignKey('driver.id')),
    extend_existing=True
)
route_bus = db.Table(
    'route_bus',
    db.Column('route_id', db.Integer, db.ForeignKey('route.id')),
    db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
    extend_existing=True
)


class Bus(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "bus"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    capacity: int = db.Column(db.Integer)
    age: int = db.Column(db.Integer)
    run: int = db.Column(db.Integer)
    is_own: int = db.Column(db.Integer)

    # Many-to-Many relationship with Driver
    drivers = db.relationship('Driver', secondary=bus_driver,
                                         backref=db.backref('buses_associated', lazy='dynamic'))
    routes = db.relationship('Route', secondary=route_bus, backref=db.backref('buses_association', lazy='dynamic'))

    def __repr__(self) -> str:
        return f"Bus({self.id}, {self.capacity}, {self.run}, {self.age}, {self.is_own})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as a dictionary
        """
        return {
            "id": self.id,
            "capacity": self.capacity,
            "run": self.run,
            "age": self.age,
            "is_own": self.is_own,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Bus:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Bus(
            capacity=dto_dict.get("capacity"),
            run=dto_dict.get("run"),
            age=dto_dict.get("age"),
            is_own=dto_dict.get("is_own")
        )
        return obj
