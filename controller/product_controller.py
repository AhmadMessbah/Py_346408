from model.entity.product import Product
from model.service.product_service import ProductService


class ProductController:
    def save(self, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            service = ProductService()
            service.save(product)
            return True, f"Product Saved Successfully \n{product}"
        except:
            return False, "Save Error"

    def update(self, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            service = ProductService()
            service.update(product)
            return True, f"Product Saved Successfully \n{product}"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = ProductService()
            service.delete(id)
            return True, f"Product with Id {id} delete successfully"
        except:
            return False, "delete Error"

    def find_all(self):
        try:
            service = ProductService()
            product_list = service.find_all(self)
            return True, product_list
        except:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = ProductService()
            product = service.find_by_id(id)
            return True, product
        except:
            return False, "Find By Id Error"
