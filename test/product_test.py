from model.entity.product import Product
from model.service.product_service import ProductService

product = Product(1, "mobile", "iPhon", "13pro", "123a","electric","12",None)

service = ProductService()

#test passed
# service.save(product)

#service.update(product)

#service.delete(1)

#print(service.find_all())

#print(service.find_by_id(2))