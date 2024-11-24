from flask import Blueprint, request
from marshmallow import ValidationError
from .services import ProductoService, ResponseBuilder
from .mapping import ProductoSchema, ResponseSchema

producto_schema = ProductoSchema()
producto_service = ProductoService()
response_schema = ResponseSchema()

catalogo = Blueprint('catalogo', __name__)


@catalogo.route('/productos', methods=['GET'])
def get_all():
    response_builder = ResponseBuilder()
    data = producto_schema.dump(producto_service.all(), many=True)
    response_builder.add_message("Productos found").add_status_code(200).add_data(data)
    return response_schema.dump(response_builder.build()), 200

@catalogo.route('/productos/add', methods=['POST'])
def add():
    response_builder = ResponseBuilder()
    try:
        producto = producto_schema.load(request.json)
        data = producto_schema.dump(producto_service.add(producto))
        response_builder.add_message("Producto added").add_status_code(201).add_data(data)
        return response_schema.dump(response_builder.build()), 201
    except ValidationError as err:
        response_builder.add_message("Validation error").add_status_code(422).add_data(err.messages)
        return response_schema.dump(response_builder.build()), 422

@catalogo.route('/productos/<int:id>', methods=['GET'])
def find_activo(id):
    response_builder = ResponseBuilder()
    producto = producto_service.find_activo(id)
    if producto:
        data = producto_schema.dump(producto)
        response_builder.add_message("Producto found").add_status_code(200).add_data(data)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message("Producto not found").add_status_code(404).add_data({'id': id})
        return response_schema.dump(response_builder.build()), 404

