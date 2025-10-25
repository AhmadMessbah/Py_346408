from model import Delivery
from service import DeliveryService
from tools.logging import Logger


class DeliveryController:
    delivery_service = DeliveryService()

    @classmethod
    def save(cls, first_name, last_name, address, description):
        try:
            delivery = Delivery(None, first_name, last_name, address, description)
            delivery = cls.delivery_service.save(delivery)
            Logger.info(f"Delivery {delivery} saved")
            return True, f"Delivery Saved Successfully"
        except Exception as e:
            Logger.error(f"Delivery Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, delivery_id, first_name, last_name, address, description):
        try:
            delivery = Delivery(delivery_id, first_name, last_name, address, description)
            delivery = cls.delivery_service.update(delivery)
            Logger.info(f"Delivery {delivery} updated")
            return True, "Delivery Updated Successfully"
        except Exception as e:
            Logger.error(f"Delivery Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, delivery_id):
        try:
            delivery = cls.delivery_service.delete(delivery_id)
            Logger.info(f"Delivery {delivery} deleted")
            return True, f"Delivery Deleted Successfully"
        except Exception as e:
            Logger.error(f"Delivery Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            delivery_list = cls.delivery_service.find_all()
            Logger.info("Delivery FindAll")
            return True, delivery_list
        except Exception as e:
            Logger.error(f"Delivery FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, delivery_id):
        try:
            delivery = cls.delivery_service.find_by_id(delivery_id)
            Logger.info(f"Delivery FindById {delivery_id}")
            return True, delivery
        except Exception as e:
            Logger.error(f"Delivery FindById Error: {e}")
            return False, e
