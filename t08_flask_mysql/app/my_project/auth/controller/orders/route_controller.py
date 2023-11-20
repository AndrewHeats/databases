"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import route_service
from my_project.auth.controller.general_controller import GeneralController


class RouteController(GeneralController):
    """
    Realisation of Route controller.
    """
    _service = route_service
