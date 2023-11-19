"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""
from .orders.driver_service import DriverService
from .orders.bus_service import BusService
from .orders.client_service import ClientService
from .orders.client_type_service import ClientTypeService
from .orders.ticket_service import TicketService
from .orders.stop_service import StopService

driver_service = DriverService()
bus_service = BusService()
client_service = ClientService()
client_type_service = ClientTypeService()
ticket_service = TicketService()
stop_service = StopService()
