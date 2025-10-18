from model.entity.delivery import Delivery
from model.service.delivery_service import DeliveryService

delivery = Delivery(1, "Hossein", "Hosseini", "street 26", "Tozih jadid")

delivery_service = DeliveryService()

#test failed
delivery_service.save(delivery)

#test failed
#delivery_service.update(delivery)

#test failed
#delivery_service.delete(1)

