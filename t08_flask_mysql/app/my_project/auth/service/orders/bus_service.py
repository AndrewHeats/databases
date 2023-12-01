

from my_project.auth.dao import bus_dao
from my_project.auth.service.general_service import GeneralService


class BusService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = bus_dao
    def find_drivers(self, bus_id: int):
        return self._dao.find_drivers(bus_id)
    def find_routes(self, bus_id: int):
        return self._dao.find_routes(bus_id)