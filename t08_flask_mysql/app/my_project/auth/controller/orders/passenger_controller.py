from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import passenger_service


class PassengerController(GeneralController):
    """
    Realisation of Passenger controller.
    """
    _service = passenger_service

    def find_routes(self, passenger_id: int):
        return self._service.find_routes(passenger_id)

