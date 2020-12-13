from .schemas import InventorySchema
from main.database import db
from .models import Inventory
from marshmallow import ValidationError


class InventoryController(object):
    schemas = InventorySchema(many=True)
    schema = InventorySchema()

    def create(self, code, type, assignee):
        json_input = {
            "code": code,
            "type": type,
            "assignee": assignee,
        }
        try:
            inventory = self.schema.load(json_input)
        except ValidationError as err:
            return {"errors": err.messages}, 422

        db.session.add(inventory)
        db.session.commit()

        return self.dump(inventory), 201

    def update_by_code(self, code, type, assignee, update_by_code=None):
        json_input = {
            "code": code,
            "type": type,
            "assignee": assignee,
        }

        if not update_by_code:
            update_by_code = json_input.get("code")

        instance = Inventory.query.filter_by(code=update_by_code).first()

        if not instance:
            return {"errors": f"Invalid inventory code: {code}"}, 422

        try:
            inventory = self.schema.load(json_input, instance=instance)
        except ValidationError as err:
            return {"errors": err.messages}, 422

        db.session.add(inventory)
        db.session.commit()

        return self.dump(inventory), 202

    def dump(self, instance):
        return self.schema.dump(instance)

    def dump_list(self, instances):
        return self.schemas.dump(instances)

    def get_all_inventory(self):
        return self.dump_list(Inventory.query.all())

    def get_inventory_by_code(self, code):
        return self.dump(Inventory.query.filter_by(code=code).first())