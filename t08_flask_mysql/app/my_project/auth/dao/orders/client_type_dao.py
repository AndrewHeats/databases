"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import ClientType


class ClientTypeDAO(GeneralDAO):
    """
    Realisation of ClientType data access layer.
    """
    _domain_type = ClientType
