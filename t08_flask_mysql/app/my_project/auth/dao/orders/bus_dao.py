

from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Bus

from my_project.auth.domain.orders.driver import driver_bus

from my_project.auth.domain.orders.driver import Driver

from my_project.auth.domain.orders.bus import route_bus
from my_project.auth.domain.orders.route import Route


class BusDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Bus
    def find_drivers(self, bus_id: int) :
        """
        Find buses associated with a specific driver.
        :param bus_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        driver_ids = (
            session.query(driver_bus.c.driver_id)
            .filter(driver_bus.c.bus_id == bus_id)
            .all()
        )

        # Extract bus IDs from the result
        driver_ids = [driver_id for (driver_id,) in driver_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        drivers = session.query(Driver).filter(Driver.id.in_(driver_ids)).all()

        return [driver.put_into_dto() for driver in drivers]

    def find_routes(self, bus_id: int):
        """
        Find buses associated with a specific driver.
        :param bus_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        route_ids = (
            session.query(route_bus.c.route_id)
            .filter(route_bus.c.bus_id == bus_id)
            .all()
        )

        # Extract bus IDs from the result
        route_ids = [route_id for (route_id,) in route_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        routes = session.query(Route).filter(Route.id.in_(route_ids)).all()

        return [route.put_into_dto() for route in routes]
