import re
def product_name_validator(product_name):
    if not (type(product_name) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", product_name)):
        raise ValueError("Invalid product_name !!!")
    else:
        return product_name

def product_type_validator(product_type):
    if not (type(product_type) == str and re.match(r"^[a-zA-Z0-9\s]{1,30}$", product_type)):
        raise ValueError("Invalid product_type !!!")
    else:
        return product_type

def expiration_date_validator(expiration_date):
    if not (type(expiration_date) == str and re.match(r"^\d{4}-\d{2}-\d{2}$", expiration_date)):
        raise ValueError("Invalid expiration_date !!!")
    else:
        return expiration_date

def warehouse_code_validator(warehouse_code):
    if not (type(warehouse_code) == str and re.match(r"^[a-zA-Z0-9\s]{1,7}$", warehouse_code)):
        raise ValueError("Invalid warehouse_code !!!")
    else:
        return warehouse_code

def unit_price_validator(unit_price):
    if not (type(unit_price) == str and re.match(r"^[0-9\s]{1,10}$", unit_price)):
        raise ValueError("Invalid unit_price !!!")
    else:
        return unit_price
def stock_quantity_validator(stock_quantity):
    if not (type(stock_quantity) == int and re.match(r"^[0-9\s]{1,7}$", stock_quantity)):
        raise ValueError("Invalid stock_quantity !!!")
    else:
        return stock_quantity
