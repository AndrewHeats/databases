"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Stop(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "stop"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address: str = db.Column(db.String(40))




    def __repr__(self) -> str:
        return f"Bus({self.id}, {self.address})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "address": self.address,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Stop:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Stop(
            address=dto_dict.get("address"),

        )
        return obj
