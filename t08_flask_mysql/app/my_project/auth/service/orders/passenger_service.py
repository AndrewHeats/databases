

from my_project.auth.dao import passenger_dao
from my_project.auth.service.general_service import GeneralService


class PassengerService(GeneralService):
    """
    Realisation of Passenger service.
    """
    _dao = passenger_dao
    def find_routes(self, passenger_id: int):
        return self._dao.find_routes(passenger_id)
