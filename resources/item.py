# import uuid
# from flask import request
# from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from sqlalchemy.exc import SQLAlchemyError


# from db import db
# from models import ItemModel
# from schemas import ItemSchema, ItemUpdateSchema


# blp = Blueprint("Items", "items", description="Operations on items")


# @blp.route("/item/<string:item_id>")
# class Item(MethodView):
#     @blp.response(200, ItemSchema)
#     def get(self, item_id):
#         # try:
#         #     return items[item_id]
#         # except KeyError:
#         #     abort(404, message="Item not found.")
#         item = ItemModel.query.get_or_404(item_id)
#         return item

#     def delete(self, item_id):
#         # try:
#         #     del items[item_id]
#         #     return {"message": "Item deleted."}
#         # except KeyError:
#         #     abort(404, message="Item not found.")
#         # item = ItemModel.query.get_or_404(item_id)
#         # raise NotImplementedError("Deleting an item is not implemented.")
#         db.session.delete(item)
#         db.session.commit()
#         return {"message": "Item deleted."}

#     @blp.arguments(ItemUpdateSchema)
#     @blp.response(200, ItemSchema)
#     def put(self, item_data, item_id):
#         # try:
#         #     item = items[item_id]

#         #     # https://blog.teclado.com/python-dictionary-merge-update-operators/
#         #     item |= item_data # |= means to update the item 

#         #     return item
#         # except KeyError:
#         #     abort(404, message="Item not found.")
#         # item = ItemModel.query.get_or_404(item_id)
#         # raise NotImplementedError("Updating an item is not implemented.")
#         item = ItemModel.query.get(item_id)
#         if item:
#             item.price = item_data["price"]
#             item.name = item_data["name"]
#         else:
#             item = ItemModel(id=item_id, **item_data)

#         db.session.add(item)
#         db.session.commit()

#         return item


# @blp.route("/item")
# class ItemList(MethodView):
#     @blp.response(200, ItemSchema(many=True))
#     def get(self):
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import ItemModel
from schemas import ItemSchema, ItemUpdateSchema

blp = Blueprint("Items", "items", description="Operations on items")


@blp.route("/item/<string:item_id>")
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item

    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        # raise NotImplementedError("Deleting an item is not implemented.")
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted."}

    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, item_data, item_id):

        item = ItemModel.query.get(item_id)
        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)

        db.session.add(item)
        db.session.commit()

        return item

@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)

        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return item

