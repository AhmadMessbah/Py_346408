from model.entity.product import Product
from model.service.product_service import ProductService


class ProductController:
    def save(self, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            print("zakhire shod, ok")
            service = ProductService()
            service.save(product)
            return True, "Saved"
        except:
            return False, "Save Error"

    def update(self, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            print("beruz shod, ok")
            service = ProductService()
            service.update(product)
            return True, "Updated"
        except:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = ProductService()
            service.delete(id)
            return True, f"Deleted {id}"
        except:
            return False, "Delete Error"

    def find_all(self):
        try:
            service = ProductService()
            service.find_all(self)
            return True, "All Products"
        except:
            return False, "Found Error"

    def find_by_id(self, id):
        try:
            service = ProductService()
            service.find_by_id(self, id)
            return True, f"Product With {id} Found"
        except:
            return False, "Found Error"
