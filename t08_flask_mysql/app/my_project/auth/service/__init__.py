"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from .orders.driver_service import DriverService
from .orders.bus_service import BusService
from .orders.client_service import ClientService
from .orders.client_type_service import ClientTypeService
from .orders.route_service import RouteService
from .orders.subroute_service import SubrouteService
from .orders.ticket_service import TicketService
from .orders.stop_service import StopService
from .orders.passenger_service import PassengerService

driver_service = DriverService()
bus_service = BusService()
client_service = ClientService()
client_type_service = ClientTypeService()
ticket_service = TicketService()
stop_service = StopService()
passenger_service = PassengerService()
route_service = RouteService()
subroute_service = SubrouteService()
