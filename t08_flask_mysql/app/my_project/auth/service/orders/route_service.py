"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao import route_dao
from my_project.auth.service.general_service import GeneralService


class RouteService(GeneralService):
    """
    Realisation of Route service.
    """
    _dao = route_dao
