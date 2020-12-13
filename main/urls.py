from .app import app
from flask_restx import Api
from inventory.resources import InventoryResource

# start API
api = Api(app, prefix="/")

api.add_resource(InventoryResource, "/inventory", "/inventory/<inventory_code>")
