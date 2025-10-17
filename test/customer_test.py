from model.entity.customer import Customer
from model.service.customer_service import CustomerService


customer = Customer(1, "reza", "alii", "091234867890", "street2, number2")

customer_service = CustomerService()

#test passed
#customer_service.save(customer)

#test passed
#customer_service.update(customer)

#test passed
#customer_service.delete(1)

#test passed
#print(customer_service.find_all())

#test passed
#print(customer_service.find_by_id(10))
