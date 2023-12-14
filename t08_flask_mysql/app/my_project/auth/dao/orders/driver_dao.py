from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Driver, Bus
from my_project.auth.domain.orders.driver import driver_bus


class DriverDAO(GeneralDAO):
    """
    Realisation of Driver data access layer.
    """
    _domain_type = Driver

    def find_buses(self, driver_id: int) -> List[Bus]:
        """
        Find buses associated with a specific driver.
        :param driver_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        bus_ids = (
            session.query(driver_bus.c.bus_id)
            .filter(driver_bus.c.driver_id == driver_id)
            .all()
        )

        # Extract bus IDs from the result
        bus_ids = [bus_id for (bus_id,) in bus_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        buses = session.query(Bus).filter(Bus.id.in_(bus_ids)).all()

        return [bus.put_into_dto() for bus in buses]

    """
    procedure section
    """

    def procedure_insert_driver(self, name, surname, company):
        try:
            result = self._session.execute(sqlalchemy.text("CALL flixbus.insert_driver(:p1, :p2, :p3)"),
                                           {"p1": name, "p2": surname, "p3": company})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None

    def insert_driver_bus_dependency_by_name_and_run(self, name, run):
        try:
            result = self._session.execute(
                sqlalchemy.text("CALL flixbus.insert_driver_bus_dependency_by_name_and_run(:p1, :p2)"),
                {"p1": name, "p2": run})
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None

    def insert_data(self):
        try:
            result = self._session.execute(sqlalchemy.text("CALL flixbus.insert_data()"))
            self._session.commit()
            return result.mappings()
        except Exception as e:
            print(f"Error executing stored procedure: {e}")
            self._session.rollback()
            return None
