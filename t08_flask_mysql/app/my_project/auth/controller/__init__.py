"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.driver_controller import DriverController
from .orders.bus_controller import BusController
from .orders.client_controller import ClientController
from .orders.client_type_controller import ClientTypeController
from .orders.passenger_controller import PassengerController
from .orders.route_controller import RouteController
from .orders.stop_controller import StopController
from .orders.subroute_controller import SubrouteController
from .orders.ticket_controller import TicketController

driver_controller = DriverController()
bus_controller = BusController()
client_controller = ClientController()
client_type_controller = ClientTypeController()
ticket_controller = TicketController()
stop_controller = StopController()
passenger_controller = PassengerController()
route_controller = RouteController()
subroute_controller = SubrouteController()
