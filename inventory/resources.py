# -*- coding: utf-8 -*-
from __future__ import absolute_import
from flask_restx import Resource
from .models import Inventory
from .controllers import InventoryController
from flask import request
from flask import jsonify


class InventoryResource(Resource):
    controller = InventoryController()

    def get(self):
        return self.controller.get_all_inventory()

    def post(self):
        json_input = request.get_json()
        return self.controller.create(**json_input)

    def put(self, inventory_code):
        json_input = request.get_json()
        return self.controller.update_by_code(
            update_by_code=inventory_code, **json_input
        )
