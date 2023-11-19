"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import driver_service
from my_project.auth.controller.general_controller import GeneralController


class DriverController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = driver_service