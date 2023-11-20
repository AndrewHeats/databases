

from my_project.auth.dao import bus_dao
from my_project.auth.service.general_service import GeneralService


class BusService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = bus_dao
