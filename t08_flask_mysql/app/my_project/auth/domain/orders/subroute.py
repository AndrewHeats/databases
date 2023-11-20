from __future__ import annotations
from typing import Dict, Any
from my_project import db
from my_project.auth.domain.i_dto import IDto


class Subroute(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "subroute"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    distance_of_subroute = db.Column(db.Integer)
    price_of_subroute = db.Column(db.Integer)

    start_of_subroute = db.Column(db.Integer, db.ForeignKey('stop.id'), nullable=True)
    end_of_subroute = db.Column(db.Integer, db.ForeignKey('stop.id'), nullable=True)

    route_id = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)  # Foreign key for Route
    route = db.relationship('Route', backref='subroutes', lazy=True)

    start = db.relationship('Stop', foreign_keys=[start_of_subroute], lazy=True, uselist=False,
                            backref='start_subroute')
    end = db.relationship('Stop', foreign_keys=[end_of_subroute], lazy=True, uselist=False, backref='end_subroute')

    def __repr__(self) -> str:
        return f"Subroute({self.id}, {self.distance_of_subroute}, {self.price_of_subroute}, " \
               f"{self.start_of_subroute}, {self.end_of_subroute}, route_id={self.route_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "distance_of_subroute": self.distance_of_subroute,
            "price_of_subroute": self.price_of_subroute,
            "start": self.start.put_into_dto() if self.start is not None else None,
            "end": self.end.put_into_dto() if self.end is not None else None,
            "start_of_subroute": self.start.address if self.start is not None else "",
            "end_of_subroute": self.end.address if self.end is not None else "",
            "route_id": self.route_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Subroute:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Subroute(
            distance_of_subroute=dto_dict.get("distance_of_subroute"),
            price_of_subroute=dto_dict.get("price_of_subroute"),
            start_of_subroute=dto_dict.get("start"),
            end_of_subroute=dto_dict.get("end"),
            route_id=dto_dict.get("route_id"),
        )
        return obj
