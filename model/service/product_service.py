from model import ProductRepository


class ProductService:
    def __init__(self):
        self.repository = ProductRepository()

    def save(self, product):
        return self.repository.save(product)

    def update(self, product):
        product_result = self.repository.find_by_id(product.id)
        if product_result:
            self.repository.update(product)
            return product
        else:
            raise Exception("Product Not Found !!!")

    def delete(self, product_id):
        product = self.repository.find_by_id(product_id)
        if product:
            self.repository.delete(product_id)
            return product
        else:
            raise Exception("Product Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, product_id):
        product = self.repository.find_by_id(product_id)
        if product:
            return product
        else:
            raise Exception("Product Not Found !!!")

    def find_by_name_and_brand(self,name,brand):
        return self.repository.find_by_name_and_brand(name,brand)

    def find_by_category(self,category):
        return self.repository.find_by_category(category)

    def find_by_expire_date_until(self,expire_date):
        return self.repository.find_by_expire_date_until(expire_date)