"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.bus_dao import BusDAO
from .orders.driver_dao import DriverDAO
from .orders.client_dao import ClientDAO
from .orders.client_type_dao import ClientTypeDAO
from .orders.route_dao import RouteDAO
from .orders.stop_dao import StopDAO
from .orders.subroute_dao import SubrouteDAO
from .orders.ticket_dao import TicketDAO
from .orders.passenger_dao import PassengerDAO

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
bus_dao = BusDAO()
driver_dao = DriverDAO()
stop_dao = StopDAO()
ticket_dao = TicketDAO()
passenger_dao = PassengerDAO()
route_dao = RouteDAO()
subroute_dao = SubrouteDAO()