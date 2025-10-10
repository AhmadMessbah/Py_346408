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

    def update(self, product):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass
