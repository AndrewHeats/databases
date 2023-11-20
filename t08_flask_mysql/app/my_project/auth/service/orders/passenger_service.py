"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao import passenger_dao
from my_project.auth.service.general_service import GeneralService


class PassengerService(GeneralService):
    """
    Realisation of Passenger service.
    """
    _dao = passenger_dao
