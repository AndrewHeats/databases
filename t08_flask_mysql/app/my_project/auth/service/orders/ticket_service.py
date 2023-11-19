from t08_flask_mysql.app.my_project.auth.dao import ticket_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TicketService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = ticket_dao
