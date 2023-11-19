"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import driver_controller
from my_project.auth.domain import Driver

driver_bp = Blueprint('drivers', __name__, url_prefix='/drivers')


@driver_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_all()), HTTPStatus.OK)


@driver_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.create(driver)
    return make_response(jsonify(driver.put_into_dto()), HTTPStatus.CREATED)


@driver_bp.get('/<int:driver_id>')
def get_client(driver_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(driver_controller.find_by_id(driver_id)), HTTPStatus.OK)


@driver_bp.put('/<int:driver_id>')
def update_client(driver_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    driver = Driver.create_from_dto(content)
    driver_controller.update(driver_id, driver)
    return make_response("Driver updated", HTTPStatus.OK)


@driver_bp.patch('/<int:bus_id>')
def patch_client(bus_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    driver_controller.patch(bus_id, content)
    return make_response("Bus updated", HTTPStatus.OK)


@driver_bp.delete('/<int:bus_id>')
def delete_client(bus_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    driver_controller.delete(bus_id)
    return make_response("Bus deleted", HTTPStatus.OK)
