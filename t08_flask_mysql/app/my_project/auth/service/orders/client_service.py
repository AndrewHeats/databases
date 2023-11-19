"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao import client_dao
from my_project.auth.service.general_service import GeneralService


class ClientService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = client_dao
