from model import Delivery, DeliveryService


class DeliveryController:
    def save(self, first_name, last_name, address, description):
        try:
            delivery = Delivery(None, first_name, last_name, address, description)
            service = DeliveryService()
            service.save(delivery)
            return True, "Saved"
        except Exception as e:
            return False, e

    def update(self, id, first_name, last_name, address, description):
        try:
            delivery = Delivery(id, first_name, last_name, address, description)
            service = DeliveryService()
            service.update(delivery)
            return True, "Updated"
        except Exception as e:
            return False, e

    def delete(self, id):
        try:
            service = DeliveryService()
            service.delete(id)
            return True, "Deleted"
        except Exception as e:
            return False, e

    def find_all(self):
        try:
            service = DeliveryService()
            return True, service.find_all()
        except Exception as e:
            return False, e

    def find_by_id(self, id):
        try:
            service = DeliveryService()
            return True, service.find_by_id(id)
        except Exception as e:
            return False, e
