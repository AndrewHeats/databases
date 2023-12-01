

from my_project.auth.service import subroute_service
from my_project.auth.controller.general_controller import GeneralController


class SubrouteController(GeneralController):
    """
    Realisation of Route controller.
    """
    _service = subroute_service
