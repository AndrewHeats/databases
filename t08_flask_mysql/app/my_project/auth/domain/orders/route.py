from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto

route_bus = db.Table(
    'route_bus',
    db.Column('route_id', db.Integer, db.ForeignKey('route.id')),
    db.Column('bus_id', db.Integer, db.ForeignKey('bus.id')),
    extend_existing=True
)


class Route(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    distance_between_2_stops = db.Column(db.Integer)
    number_of_stops = db.Column(db.Integer)

    # Foreign keys for start and end stops
    start_of_the_route = db.Column(db.Integer, db.ForeignKey('stop.id'), nullable=True)
    end_of_the_route = db.Column(db.Integer, db.ForeignKey('stop.id'), nullable=True)

    # Relationships for start and end stops
    start = db.relationship('Stop', foreign_keys=[start_of_the_route], lazy=True, uselist=False, backref='start_route')
    end = db.relationship('Stop', foreign_keys=[end_of_the_route], lazy=True, uselist=False, backref='end_route')

    buses = db.relationship('Bus', secondary=route_bus, backref=db.backref('routes_association', lazy='dynamic'))

    @property
    def distance_of_route(self):
        return (self.number_of_stops - 1) * self.distance_between_2_stops

    def __repr__(self) -> str:
        return f"Route({self.id}, {self.distance_of_route}, {self.number_of_stops}, " \
               f"{self.start_of_the_route}, {self.end_of_the_route}, {self.distance_between_2_stops})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "number_of_stops": self.number_of_stops,
            "distance_between_2_stops": self.distance_between_2_stops,
            "distance_of_route": self.distance_of_route,
            "start_of_the_route": self.start.address if self.start is not None else "",
            "end_of_the_route": self.end.address if self.end is not None else "",
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Route:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Route(
            number_of_stops=dto_dict.get("number_of_stops"),
            distance_between_2_stops=dto_dict.get("distance_between_2_stops"),
            start_of_the_route=dto_dict.get("start"),
            end_of_the_route=dto_dict.get("end"),
        )
        return obj
