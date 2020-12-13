from main.database import ma, db
from flask_restx import fields
from .models import Inventory


class InventorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inventory
        fields = ("code", "type", "assignee")
        load_instance = True
