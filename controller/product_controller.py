from model import Product, ProductService
from tools.logging import Logger


class ProductController:
    product_service = ProductService()

    @classmethod
    def save(cls, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(None, name, brand, model, serial, category, unit, expiration_date)
            product = cls.product_service.save(product)
            Logger.info(f"Product {product} saved")
            return True, f"Product Saved Successfully"
        except Exception as e:
            Logger.error(f"Product Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, product_id, name, brand, model, serial, category, unit, expiration_date):
        try:
            product = Product(product_id, name, brand, model, serial, category, unit, expiration_date)
            product = cls.product_service.update(product)
            Logger.info(f"Product {product} updated")
            return True, "Product Updated Successfully"
        except Exception as e:
            Logger.error(f"Product Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, product_id):
        try:
            product = cls.product_service.delete(product_id)
            Logger.info(f"Product {product} deleted")
            return True, f"Product Deleted Successfully"
        except Exception as e:
            Logger.error(f"Product Delete Error: {e}")
            return False, e

    def find_all(self):
        try:
            product_list = cls.product_service.find_all()
            Logger.info("Product FindAll")
            return True, product_list
        except Exception as e:
            Logger.error(f"Product FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, product_id):
        try:
            product = cls.product_service.find_by_id(product_id)
            Logger.info(f"Product FindById {product_id}")
            return True, product
        except Exception as e:
            Logger.error(f"Product FindById Error: {e}")
            return False, e

    @classmethod
    def find_by_name_and_brand(cls, name, brand):
        try:
            product_list = cls.product_service.find_by_name_and_brand(name, brand)
            Logger.info(f"Product FindByNameAndBrand {name} {brand}")
            return True, product_list
        except Exception as e:
            Logger.error(f"Product FindByNameAndBrand Error: {e}")
            return False, e

    @classmethod
    def find_by_category(cls, category):
        try:
            product_list = cls.product_service.find_by_category(category)
            Logger.info(f"Product FindByCategory {category}")
            return True, product_list
        except Exception as e:
            Logger.error(f"Product FindByCategory Error: {e}")
            return False, e

    @classmethod
    def find_by_expire_date_until(cls, expire_date):
        try:
            product_list = cls.product_service.find_by_expire_date_until(expire_date)
            Logger.info(f"Product FindByExpireDateUntil {expire_date}")
            return True, product_list
        except Exception as e:
            Logger.error(f"Product FindByExpireDateUntil Error: {e}")
            return False, e
