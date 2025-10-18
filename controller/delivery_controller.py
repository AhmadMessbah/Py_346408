from model.entity.delivery import Delivery
from model.service.delivery_service import DeliveryService


class DeliveryController:
    def save(self, first_name, last_name, address, description):
        try:
            delivery = Delivery(None, first_name, last_name, address, description)
            service = DeliveryService()
            service.save(delivery)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, id, first_name, last_name, address, description):
        try:
            delivery = Delivery(id, first_name, last_name, address, description)
            service = DeliveryService()
            service.update(delivery)
            return True, "Updated"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = DeliveryService()
            service.delete(id)
            return True, "Deleted"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = DeliveryService()
            service.find_all()
            return True, "Found"
        except:
            return False, "Error"

    def find_by_id(self, id):
        try:
            service = DeliveryService()
            service.find_by_id(id)
            return True, "Found"
        except:
            return False, "Error"
