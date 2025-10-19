from model.entity.product import Product
from model.service.product_service import ProductService

product = Product(1, "mobile", "iPhone", "13pro", "123a","electronic","12",None)

product_service = ProductService()

#test passed
# service.save(product)

#test passed
#service.update(product)

#test passed
#service.delete(1)

#test passed
#print(service.find_all())

#test passed
#print(service.find_by_id(2))