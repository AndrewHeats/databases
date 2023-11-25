
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import bus_controller
from my_project.auth.domain import Bus

bus_bp = Blueprint('buses', __name__, url_prefix='/buses')


@bus_bp.get('')
def get_all_clients() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(bus_controller.find_all()), HTTPStatus.OK)

@bus_bp.get('/<int:bus_id>/drivers')
def get_all_buses_from_drivers(bus_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(bus_controller.find_drivers(bus_id)), HTTPStatus.OK)

@bus_bp.get('/<int:bus_id>/routes')
def get_all_buses_from_routes(bus_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(bus_controller.find_routes(bus_id)), HTTPStatus.OK)

@bus_bp.post('')
def create_client() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    bus = Bus.create_from_dto(content)
    bus_controller.create(bus)
    return make_response(jsonify(bus.put_into_dto()), HTTPStatus.CREATED)


@bus_bp.get('/<int:bus_id>')
def get_client(bus_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(bus_controller.find_by_id(bus_id)), HTTPStatus.OK)


@bus_bp.put('/<int:bus_id>')
def update_client(bus_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    bus = Bus.create_from_dto(content)
    bus_controller.update(bus_id, bus)
    return make_response("Bus updated", HTTPStatus.OK)


@bus_bp.patch('/<int:bus_id>')
def patch_client(bus_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    bus_controller.patch(bus_id, content)
    return make_response("Bus updated", HTTPStatus.OK)


@bus_bp.delete('/<int:bus_id>')
def delete_client(bus_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    bus_controller.delete(bus_id)
    return make_response("Bus deleted", HTTPStatus.OK)
