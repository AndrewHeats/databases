"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import passenger_controller
from my_project.auth.domain import Passenger

passenger_bp = Blueprint('passengers', __name__, url_prefix='/passengers')


@passenger_bp.get('')
def get_all_passengers() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(passenger_controller.find_all()), HTTPStatus.OK)


@passenger_bp.post('')
def create_passenger() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    passenger = Passenger.create_from_dto(content)
    passenger_controller.create(passenger)
    return make_response(jsonify(passenger.put_into_dto()), HTTPStatus.CREATED)


@passenger_bp.get('/<int:passenger_id>')
def get_passenger(passenger_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(passenger_controller.find_by_id(passenger_id)), HTTPStatus.OK)


@passenger_bp.put('/<int:passenger_id>')
def update_client(passenger_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    passenger = Passenger.create_from_dto(content)
    passenger_controller.update(passenger_id, passenger)
    return make_response("Passenger updated", HTTPStatus.OK)


@passenger_bp.patch('/<int:passenger_id>')
def patch_client(passenger_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    passenger_controller.patch(passenger_id, content)
    return make_response("Passenger updated", HTTPStatus.OK)


@passenger_bp.delete('/<int:passenger_id>')
def delete_client(passenger_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    passenger_controller.delete(passenger_id)
    return make_response("Passenger deleted", HTTPStatus.OK)
