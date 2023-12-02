from __future__ import annotations

from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class TicketBase(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "ticket_base"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_amount: int = db.Column(db.Integer)
    ticket_id = db.Column(db.Integer, db.ForeignKey("ticket.id"), nullable=False)

    ticket = db.Relationship("Ticket", backref="ticket_bases")

    def __repr__(self) -> str:
        return f"Ticket Base({self.id}, {self.ticket_amount}, {self.ticket.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "ticket_amount": self.ticket_amount,
            "ticket": self.ticket.price if self.ticket_id is not None else "",

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TicketBase:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TicketBase(
            ticket_amount=dto_dict.get("ticket_amount"),
            ticket_id=dto_dict.get("ticket_id")
        )
        return obj
