from model.entity.payment import Payment
from model.service.payment_service import PaymentService

payment1 = Payment(1, "receive", "cash", "2025-02-02", 12,200,11,"daryaftshod")

payment2= Payment(2, "pay", "cart", "2025-04-02", 22,250,11,"pardakhtshod")


service = PaymentService()

#test passed
#service.save(payment1)

#test passed????
#service.update(payment1)

#test passed
#service.delete(5)

#test passed
#print(service.find_all())

#test passed
#print(service.find_by_id(6))

#test did not passed
#print(service.find_by_transaction_type("receive"))

#test  did not passed
#print(service.find_by_payment_type("cash"))

#test   did not passed
#print(service.find_by_date_time_range("2025-02-02"))

#test  did not passed
#print(service.find_by_date_time_range_and_customer_id(""))

#test passed
#print(service.find_by_date_time_range_and_employee_id(""))