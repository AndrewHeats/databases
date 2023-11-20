"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import passenger_service
from my_project.auth.controller.general_controller import GeneralController


class PassengerController(GeneralController):
    """
    Realisation of Passenger controller.
    """
    _service = passenger_service