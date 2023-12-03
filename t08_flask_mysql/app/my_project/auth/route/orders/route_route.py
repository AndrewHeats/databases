from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response
from my_project.auth.controller import route_controller
from my_project.auth.domain import Route

route_bp = Blueprint('routes', __name__, url_prefix='/routes')


@route_bp.get('/<int:route_id>/buses')
def get_all_routes_from_buses(route_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_buses(route_id)), HTTPStatus.OK)


@route_bp.get('/<int:route_id>/passengers')
def get_all_routes_from_passengers(route_id) -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_passengers(route_id)), HTTPStatus.OK)


@route_bp.get('/table')
def create_table_with_timestamp() -> Response:
    result = route_controller.create_dynamic_table_with_timestamp()
    response = {"result": f"{result}, Table created successfully"}
    return make_response(jsonify(response), HTTPStatus.CREATED)


@route_bp.get('')
def get_all_routes() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


@route_bp.post('')
def create_route() -> Response:
    """
    Gets all objects from table using Service layer.
    :return: Response object
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@route_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:
    """
    Gets route by ID.
    :return: Response object
    """
    return make_response(jsonify(route_controller.find_by_id(route_id)), HTTPStatus.OK)


@route_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:
    """
    Updates client by ID.
    :return: Response object
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.update(route_id, route)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.patch('/<int:route_id>')
def patch_route(route_id: int) -> Response:
    """
    Patches client by ID.
    :return: Response object
    """
    content = request.get_json()
    route_controller.patch(route_id, content)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.delete('/<int:route_id>')
def delete_route(route_id: int) -> Response:
    """
    Deletes route by ID.
    :return: Response object
    """
    route_controller.delete(route_id)
    return make_response("Route deleted", HTTPStatus.OK)
