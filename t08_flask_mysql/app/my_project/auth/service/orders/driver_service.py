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

    def insert_driver(self, name, surname, company):
        return self._dao.insert_driver(name, surname, company)

    def insert_driver_bus_dependency_by_name_and_run(self, name, run):
        return self._dao.insert_driver_bus_dependency_by_name_and_run(name, run)

    def insert_data(self):
        return self._dao.insert_data()
