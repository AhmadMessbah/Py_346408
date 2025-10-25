from model import Delivery, DeliveryService
from tools.logging import Logger


class DeliveryController:
    def __init__(self):
        self.delivery_service = DeliveryService()

    def save(self, first_name, last_name, address, description):
        try:
            delivery = Delivery(None, first_name, last_name, address, description)
            delivery = self.delivery_service.save(delivery)
            Logger.info(f"Delivery {delivery} saved")
            return True, f"Delivery Saved Successfully"
        except Exception as e:
            Logger.error(f"Delivery Save Error: {e}")
            return False, e

    def update(self, delivery_id, first_name, last_name, address, description):
        try:
            delivery = Delivery(delivery_id, first_name, last_name, address, description)
            delivery = self.delivery_service.update(delivery)
            Logger.info(f"Delivery {delivery} updated")
            return True, "Delivery Updated Successfully"
        except Exception as e:
            Logger.error(f"Delivery Update Error: {e}")
            return False, e

    def delete(self, delivery_id):
        try:
            delivery = self.delivery_service.delete(delivery_id)
            Logger.info(f"Delivery {delivery} deleted")
            return True, f"Delivery Deleted Successfully"
        except Exception as e:
            Logger.error(f"Delivery Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            delivery_list = self.delivery_service.find_all()
            Logger.info("Delivery FindAll")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindAll Error: {e}")
            return False, e

    def find_by_id(self, delivery_id):
        try:
            delivery = self.delivery_service.find_by_id(delivery_id)
            Logger.info(f"Delivery FindById {delivery_id}")
            return True, delivery
        except Exception as e:
            Logger.error(f"Delivery FindById Error: {e}")
            return False, e
