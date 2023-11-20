
from my_project.auth.dao import subroute_dao
from my_project.auth.service.general_service import GeneralService


class SubrouteService(GeneralService):
    """
    Realisation of Subroute service.
    """
    _dao = subroute_dao
