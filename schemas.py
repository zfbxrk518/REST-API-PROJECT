
from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Str(dump_only=True) # It only be used for sending data back to the client.
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id=fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name= fields.Str()  # Optional.
    price= fields.Float()

class StoreSchema(Schema):
    id= fields.Str(dump_only=True)
    name= fields.Str(required=True)
