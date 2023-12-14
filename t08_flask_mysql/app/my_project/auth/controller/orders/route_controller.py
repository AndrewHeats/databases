

from my_project.auth.service import route_service
from my_project.auth.controller.general_controller import GeneralController


class RouteController(GeneralController):
    """
    Realisation of Route controller.
    """
    _service = route_service
    def find_buses(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._service.find_buses(route_id)

    def find_passengers(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._service.find_passengers(route_id)



