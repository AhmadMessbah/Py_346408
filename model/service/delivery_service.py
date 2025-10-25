from model import DeliveryRepository


class DeliveryService:
     def __init__(self):
         self.repository = DeliveryRepository()

     def save(self, delivery):
         return self.repository.save(delivery)

     def update(self, delivery):
         delivery_result = self.repository.find_by_id(delivery.id)
         if delivery_result:
             self.repository.update(delivery)
             return delivery
         else:
             raise Exception("Delivery Not Found !!!")

     def delete(self, delivery_id):
         delivery = self.repository.find_by_id(delivery_id)
         if delivery:
             self.repository.delete(delivery_id)
             return delivery
         else:
             raise Exception("Delivery Not Found !!!")

     def find_all(self):
         return self.repository.find_all()

     def find_by_id(self, delivery_id):
         delivery = self.repository.find_by_id(delivery_id)
         if delivery:
             return delivery
         else:
             raise Exception("Delivery Not Found !!!")

