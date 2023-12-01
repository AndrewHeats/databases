from typing import List

from my_project.auth.dao import driver_dao
from my_project.auth.service.general_service import GeneralService


class DriverService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = driver_dao

    def find_buses(self, driver_id: int):
        """
        Find buses associated with a specific driver.
        :param driver_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Call the find_buses method from the DAO
        return self._dao.find_buses(driver_id)
