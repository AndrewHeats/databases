"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from my_project.auth.service import stop_service
from my_project.auth.controller.general_controller import GeneralController


class StopController(GeneralController):
    """
    Realisation of Stop controller.
    """
    _service = stop_service
