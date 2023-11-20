
from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Subroute


class SubrouteDAO(GeneralDAO):
    """
    Realisation of Subroute data access layer.
    """
    _domain_type = Subroute

