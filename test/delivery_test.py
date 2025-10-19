from model.entity.delivery import Delivery
from model.service.delivery_service import DeliveryService
from model.repository.delivery_repository import DeliveryRepository

delivery = Delivery(None, "Hossein", "Hosseini", "street 26", "Tozih jadid")
deliv = Delivery(None, "mamad", "alipour", "street 92", "hichi")

delivery_service = DeliveryService()


repo = DeliveryRepository()
repo.update(deliv)