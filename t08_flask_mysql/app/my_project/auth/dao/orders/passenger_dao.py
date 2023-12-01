

from typing import List

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Passenger

from my_project.auth.domain.orders.passenger import route_passenger
from my_project.auth.domain.orders.route import Route


class PassengerDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Passenger

    def find_routes(self, passenger_id: int):
        """
        Find buses associated with a specific driver.
        :param passenger_id: ID of the driver
        :return: List of Bus objects associated with the driver
        """
        # Assuming that you have a session object, replace it with your actual SQLAlchemy session
        session = self.get_session()

        # Query the association table to get the bus IDs associated with the driver
        route_ids = (
            session.query(route_passenger.c.route_id)
            .filter(route_passenger.c.passenger_id == passenger_id)
            .all()
        )

        # Extract bus IDs from the result
        route_ids = [route_id for (route_id,) in route_ids]

        # Query the Bus table to get the Bus objects associated with the bus IDs
        routes = session.query(Route).filter(Route.id.in_(route_ids)).all()

        return [route.put_into_dto() for route in routes]

