

from my_project.auth.dao import route_dao
from my_project.auth.service.general_service import GeneralService


class RouteService(GeneralService):
    """
    Realisation of Route service.
    """
    _dao = route_dao

    def find_buses(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._dao.find_buses(route_id)

    def find_passengers(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._dao.find_passengers(route_id)
