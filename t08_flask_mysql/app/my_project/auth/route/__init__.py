"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.client_type_route import client_type_bp
    from .orders.bus_route import bus_bp
    from .orders.driver_route import driver_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(bus_bp)
    app.register_blueprint(client_type_bp)
    app.register_blueprint(driver_bp)
