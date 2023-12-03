
from typing import List

import sqlalchemy
from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Route

from my_project.auth.domain.orders.bus import Bus, route_bus

from my_project.auth.domain.orders.passenger import Passenger

from my_project.auth.domain.orders.passenger import route_passenger


class RouteDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Route

    def find_buses(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        bus_ids = (
            session.query(route_bus.c.bus_id)
            .filter(route_bus.c.route_id == route_id)
            .all()
        )

        # Extract bus IDs from the result
        bus_ids = [bus_id for (bus_id,) in bus_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        buses = session.query(Bus).filter(Bus.id.in_(bus_ids)).all()

        return [bus.put_into_dto() for bus in buses]


    def find_passengers(self, route_id: int):
        """
        Find buses associated with a specific driver.
        :param route_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        passengers_ids = (
            session.query(route_passenger.c.passenger_id)
            .filter(route_passenger.c.route_id == route_id)
            .all()
        )

        # Extract bus IDs from the result
        passengers_ids = [passenger_id for (passenger_id,) in passengers_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        passengers = session.query(Passenger).filter(Passenger.id.in_(passengers_ids)).all()

        return [passenger.put_into_dto() for passenger in passengers]


    def create_dynamic_table_with_timestamp(self):
        result = self._session.execute(sqlalchemy.text("CALL flixbus.create_dynamic_table_with_timestamp();"))
        self._session.commit()
        return result.mappings()


