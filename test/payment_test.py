from model.entity.payment import Payment
from model.service.payment_service import PaymentService

payment = Payment(1, "receive", "cash", "2025-02-02", 12,200,11,"daryaftshod")

service = PaymentService()

#test passed
#service.save(payment)

#test passed
#service.update(payment)

#test passed
#service.delete(1)

#test passed
#print(service.find_all())

#print(service.find_by_id(2))