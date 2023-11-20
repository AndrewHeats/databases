
from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import stop_controller
from my_project.auth.domain import Stop

stop_bp = Blueprint('stops', __name__, url_prefix='/stops')


@stop_bp.get('')
def get_all_stops() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(stop_controller.find_all()), HTTPStatus.OK)


@stop_bp.post('')
def create_stop() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    stop = Stop.create_from_dto(content)
    stop_controller.create(stop)
    return make_response(jsonify(stop.put_into_dto()), HTTPStatus.CREATED)


@stop_bp.get('/<int:stop_id>')
def get_stop(stop_id: int) -> Response:
    """
    Gets client by ID.
    :return: Response object
    """
    return make_response(jsonify(stop_controller.find_by_id(stop_id)), HTTPStatus.OK)


@stop_bp.put('/<int:stop_id>')
def update_stop(stop_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    stop = Stop.create_from_dto(content)
    stop_controller.update(stop_id, stop)
    return make_response("Stop updated", HTTPStatus.OK)


@stop_bp.patch('/<int:stop_id>')
def patch_stop(stop_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    stop_controller.patch(stop_id, content)
    return make_response("Stop updated", HTTPStatus.OK)


@stop_bp.delete('/<int:stop_id>')
def delete_stop(stop_id: int) -> Response:
    """
    Deletes client by ID.
    :return: Response object
    """
    stop_controller.delete(stop_id)
    return make_response("Stop deleted", HTTPStatus.OK)
