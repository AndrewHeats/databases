"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.driver_controller import DriverController
from .orders.bus_controller import BusController
from .orders.client_controller import ClientController
from .orders.client_type_controller import ClientTypeController

driver_controller = DriverController()
bus_controller = BusController()
client_controller = ClientController()
client_type_controller = ClientTypeController()
