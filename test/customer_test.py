from model.entity.customer import Customer
from model.service.customer_service import CustomerService
from view.customer_view import *

service = CustomerService()

customer1 = Customer(1, "reza", "rezayi", "091234867890", "street1, number1")
service.save(customer1)

customer2 = Customer(2,"sina", "zamani", "0912123434", "street2, number2")
service.save(customer2)

customer3 = Customer(3,"john", "william", "0912663434", "street3, number3")
service.save(customer3)

#print(service.find_by_firstname_and_lastname("reza", "rezayi"))

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
