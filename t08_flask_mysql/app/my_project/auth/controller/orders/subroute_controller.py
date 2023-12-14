from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import subroute_service


class SubrouteController(GeneralController):
    """
    Realisation of Route controller.
    """
    _service = subroute_service

    def make_operation(self, operation):
        return self._service.make_operation(operation)
