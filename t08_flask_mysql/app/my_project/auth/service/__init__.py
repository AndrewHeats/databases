
from .orders.driver_service import DriverService
from .orders.bus_service import BusService
from .orders.route_service import RouteService
from .orders.subroute_service import SubrouteService
from .orders.bus_base_service import BusBaseService
from .orders.ticket_service import TicketService
from .orders.stop_service import StopService
from .orders.passenger_service import PassengerService

driver_service = DriverService()
bus_service = BusService()
ticket_service = TicketService()
bus_base_service = BusBaseService()
stop_service = StopService()
passenger_service = PassengerService()
route_service = RouteService()
subroute_service = SubrouteService()
