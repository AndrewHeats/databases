from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import driver_service


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

    def procedure_insert_driver(self, name, surname, company):
        return self._service.insert_driver(name, surname, company)

    def insert_driver_bus_dependency_by_name_and_run(self, name, run):
        return self._service.insert_driver_bus_dependency_by_name_and_run(name, run)

    def insert_data(self):
        return self._service.insert_data()

