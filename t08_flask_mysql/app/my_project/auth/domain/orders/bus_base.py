from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class BusBase(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "bus_base"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    travel_count: int = db.Column(db.Integer)
    bus_id = db.Column(db.Integer,  nullable=False)



    def __repr__(self) -> str:
        return f"Ticket Base({self.id}, {self.travel_count}, {self.bus})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "travel_count": self.travel_count,
            "bus_id": self.bus_id if self.bus_id is not None else "",

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> BusBase:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = BusBase(
            travel_count=dto_dict.get("travel_count"),
            bus_id=dto_dict.get("bus_id")
        )
        return obj
