from app.models import Producto
from marshmallow import fields, Schema, post_load

class ProductoSchema(Schema):
    id = fields.Integer(dump_only=True)
    nombre = fields.String(required=True, validate=fields.Length(min=1, max=80))
    precio = fields.Float(required=True)
    activado = fields.Boolean(required=True)

    @post_load
    def make_data(self, data, **kwargs):
        return Producto(**data)