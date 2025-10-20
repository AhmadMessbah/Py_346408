from model import Product, ProductService

class ProductController:
    def save(self, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            service = ProductService()
            service.save(product)
            return True, f"Product Saved Successfully \n{product}"
        except Exception as e:
            return False, "Save Error"

    def update(self,id, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(id, name, brand, model, serial, category, unit, expiration_date)
            service = ProductService()
            service.update(product)
            return True, f"Product Saved Successfully \n{product}"
        except Exception as e:
            return False, "Update Error"

    def delete(self, id):
        try:
            service = ProductService()
            service.delete(id)
            return True, f"Product with Id {id} delete successfully"
        except Exception as e:
            return False, "delete Error"

    def find_all(self):
        try:
            service = ProductService()
            return True, service.find_all()
        except Exception as e:
            return False, "Find All Error"

    def find_by_id(self, id):
        try:
            service = ProductService()
            return True, service.find_by_id(id)
        except Exception as e:
            return False, "Find By Id Error"
