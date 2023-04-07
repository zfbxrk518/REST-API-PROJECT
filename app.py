from flask import Flask, request


app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
           {
              "name": "Chair",
              "price": 15.99
           }
        ]
    }
]
# the first endpoint or flask route: http://127.0.0.1:5000/store
@app.get("/store")
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()  # request_data is a dictionary 
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")  #   <string:name> is name of the dynamic url segment.The name parameter in the URL path is a variable placeholder that can capture the value of a string that is included in the URL at that position.
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:    #  name came from the url of insomnia
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404



@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404

@app
   