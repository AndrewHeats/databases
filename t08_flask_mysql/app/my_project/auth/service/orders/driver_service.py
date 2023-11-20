
from my_project.auth.dao import driver_dao
from my_project.auth.service.general_service import GeneralService


class DriverService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = driver_dao
