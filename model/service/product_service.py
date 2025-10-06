from model.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def save(self, product_id,
             product_name,
             product_type,
             expiration_date,
             warehouse_code,
             unit_price,
             stock_quantity):
        self.repository.save(product_id,
                             product_name,
                             product_type,
                             expiration_date,
                             warehouse_code,
                             unit_price,
                             stock_quantity)

    def update(self,
               product_id,
               product_name,
               product_type,
               expiration_date,
               warehouse_code,
               unit_price,
               stock_quantity):
        self.repository.update(product_id,
                               product_name,
                               product_type,
                               expiration_date,
                               warehouse_code,
                               unit_price,
                               stock_quantity)

    def delete(self, product_id):
        self.repository.delete(product_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, product_id):
        return self.repository.find_by_id(product_id)
