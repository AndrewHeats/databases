
from my_project.auth.service import driver_service
from my_project.auth.controller.general_controller import GeneralController


class DriverController(GeneralController):
    """
    Realisation of Client controller.
    """
    _service = driver_service
    def find_buses(self, driver_id: int):
        """
        Find buses associated with a specific driver.
        :param driver_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._service.find_buses(driver_id)