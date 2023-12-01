from t08_flask_mysql.app.my_project.auth.dao import stop_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class StopService(GeneralService):
    """
    Realisation of Stop service.
    """
    _dao = stop_dao
