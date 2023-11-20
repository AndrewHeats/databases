
from .orders.driver_controller import DriverController
from .orders.bus_controller import BusController
from .orders.passenger_controller import PassengerController
from .orders.route_controller import RouteController
from .orders.stop_controller import StopController
from .orders.subroute_controller import SubrouteController
from .orders.ticket_controller import TicketController

driver_controller = DriverController()
bus_controller = BusController()
ticket_controller = TicketController()
stop_controller = StopController()
passenger_controller = PassengerController()
route_controller = RouteController()
subroute_controller = SubrouteController()
