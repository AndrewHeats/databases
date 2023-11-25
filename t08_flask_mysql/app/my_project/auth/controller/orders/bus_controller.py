

from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import bus_service


class BusController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = bus_service

    def find_drivers(self, bus_id: int):
        return self._service.find_drivers(bus_id)

    def find_routes(self, bus_id: int):
        return self._service.find_routes(bus_id)
