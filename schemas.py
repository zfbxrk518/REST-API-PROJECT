# when we receive data and pass that data through Schema, it will say you can't send name through the API. It can only be used for returning data from the API.
from marshmallow import Schema, fields

class ItemShema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id=fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name= fields.Str()
    price= fields.Float()

class StoreSchema(Schema):
    id= fields.Str(dump_only=True)
    name= fields.Str(required=True)
