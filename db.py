# stores = {}
# items = {}
# use dictionaries will retrieve data like items[1]
# connect id with the content of the item
# so finding an item by its ID will be extremely easy if we use a dictionary for storage and not a list
# we no longer have to iterate over the entire list to find the item that we're looking for

from flask_sqlalchemy import SQLAlchemy

db =  SQLAlchemy