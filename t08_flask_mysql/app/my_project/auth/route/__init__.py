
from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.stop_route import stop_bp
    from .orders.ticket_route import ticket_bp
    from .orders.bus_route import bus_bp
    from .orders.driver_route import driver_bp
    from .orders.passenger_route import passenger_bp
    from .orders.route_route import route_bp
    from .orders.subroute_route import subroute_bp

    app.register_blueprint(bus_bp)
    app.register_blueprint(driver_bp)
    app.register_blueprint(stop_bp)
    app.register_blueprint(ticket_bp)
    app.register_blueprint(passenger_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(subroute_bp)
