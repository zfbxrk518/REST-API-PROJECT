import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import stores
from schemas import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self,store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message = "Store not found")

    def delete(self,store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError:
            abort(404, message = "Store not found")



@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200, StoreSchema(many=True))
    def get(self):
        return stores.values() 
    
    @blp.arguments(StoreSchema)
    @blp.response(201, StoreSchema)
    def post(self, store_data):
        for store in stores.values():
            if store_data["name"] == store["name"]:
                abort(400, message=f"Store already exists")

        store_id = uuid.uuid4().hex  # uuid is unique identifier, a more common way instead of <string: name>
        store = {**store_data, "id": store_id}
        # **passing keyword arguments to a construture, 
        # unpack the values in the store_data dictionary and include them in the new {**store_data, "id": store_id} dictionary,
        # add the id key as a seperate key within the dictionary
        stores[store_id] = store  # save it to the database
       
        return store
        