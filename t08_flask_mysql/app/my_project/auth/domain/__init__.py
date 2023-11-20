"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# Import here Domain Class that are needed for ORM
# orders DB
from my_project.auth.domain.orders.client import Client
from my_project.auth.domain.orders.client_type import ClientType
from my_project.auth.domain.orders.bus import Bus
from my_project.auth.domain.orders.driver import Driver
from my_project.auth.domain.orders.ticket import Ticket
from my_project.auth.domain.orders.stop import Stop
from my_project.auth.domain.orders.passenger import Passenger
from my_project.auth.domain.orders.route import Route
from my_project.auth.domain.orders.subroute import Subroute