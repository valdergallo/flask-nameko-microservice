from nameko.rpc import rpc, RpcProxy
from inventory.controllers import InventoryController


class InventoryService(object):
    name = "InventoryServices"
    controller = InventoryController()

    @rpc
    def create_inventory(self, code, type, assignee):
        return self.controller.create(code, type, assignee)

    @rpc
    def get_inventory_by_code(self, code):
        return self.controller.get_inventory_by_code(code)

    @rpc
    def get_all_inventory(self):
        return self.controller.get_all_inventory()