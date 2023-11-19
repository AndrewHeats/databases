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

client_dao = ClientDAO()
client_type_dao = ClientTypeDAO()
bus_dao = BusDAO()
driver_dao = DriverDAO()
