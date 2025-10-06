from model.repository.product_repository import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def save(self, product):
        self.repository.save(product)

    def update(self, product):
        self.repository.update(product)

    def delete(self, product_id):
        self.repository.delete(product_id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, product_id):
        return self.repository.find_by_id(product_id)
