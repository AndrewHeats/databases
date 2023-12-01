

from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import subroute_controller
from my_project.auth.domain import Subroute

subroute_bp = Blueprint('subroutes', __name__, url_prefix='/subroutes')


@subroute_bp.get('')
def get_all_subroutes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(subroute_controller.find_all()), HTTPStatus.OK)


@subroute_bp.post('')
def create_subroute() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    subroute = Subroute.create_from_dto(content)
    subroute_controller.create(subroute)
    return make_response(jsonify(subroute.put_into_dto()), HTTPStatus.CREATED)


@subroute_bp.get('/<int:subroute_id>')
def get_route(subroute_id: int) -> Response:
    """
    Gets subroute by ID.
    :return: Response object
    """
    return make_response(jsonify(subroute_controller.find_by_id(subroute_id)), HTTPStatus.OK)


@subroute_bp.put('/<int:subroute_id>')
def update_route(subroute_id: int) -> Response:
    """
    Updates subroute by ID.
    :return: Response object
    """
    content = request.get_json()
    subroute = Subroute.create_from_dto(content)
    subroute_controller.update(subroute_id, subroute)
    return make_response("Subroute updated", HTTPStatus.OK)


@subroute_bp.patch('/<int:subroute_id>')
def patch_route(subroute_id: int) -> Response:
    """
    Patches subroute by ID.
    :return: Response object
    """
    content = request.get_json()
    subroute_controller.patch(subroute_id, content)
    return make_response("Subroute updated", HTTPStatus.OK)


@subroute_bp.delete('/<int:subroute_id>')
def delete_route(subroute_id: int) -> Response:
    """
    Deletes subroute by ID.
    :return: Response object
    """
    subroute_controller.delete(subroute_id)
    return make_response("Subroute deleted", HTTPStatus.OK)
