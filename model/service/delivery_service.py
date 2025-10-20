from model import DeliveryRepository


class DeliveryService:
     def __init__(self):
         self.repository = DeliveryRepository()

     def save(self, delivery):
         self.repository.save(delivery)

     def update(self, delivery):
         self.repository.update(delivery)

     def delete(self, id):
         self.repository.delete(id)

     def find_all(self):
         return self.repository.find_all()

     def find_by_id(self, id):
         return self.repository.find_by_id(id)

