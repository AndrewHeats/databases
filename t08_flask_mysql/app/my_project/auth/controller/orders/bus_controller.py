"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import bus_service
from my_project.auth.controller.general_controller import GeneralController


class BusController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = bus_service
