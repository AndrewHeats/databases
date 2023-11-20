

from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto




class Ticket(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price: float = db.Column(db.Float(5, 2))



    def __repr__(self) -> str:
        return f"Ticket({self.id}, {self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "price": self.price,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ticket:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Ticket(
            price=dto_dict.get("price"),
        )
        return obj
