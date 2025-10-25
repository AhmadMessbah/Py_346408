from service.product_service import ProductService

service = ProductService()
# product1 = Product(1, "mobile", "iPhone", "13pro", "123a","electronic","12",None)
# service.save(product1)
#
# product2 = Product(2,"labtab","iphone", "notebook", "231a", "electronic", "13", None)
# service.save(product2)
#
# product3 = Product(3, "mobile", "samsung", "note12", "345b", "electronic", "12", None)
# service.save(product3)

#print(service.find_by_name_and_brand("mobile", "iPhone"))

print(service.find_by_name_and_brand("m", "i"))

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