import re

def product_validator(product):
    if not (type(product) == str and re.match(r"^[a-zA-Z\s]{3,30}$", product)):
        raise ValueError(f"{product} is not a valid product name")
    else:
        return product

def quantity_validator(quantity):
    if not (type(quantity) == int and re.match(r"^[0-9]{5,20}$", quantity)):
        raise ValueError(f"{quantity} is not a valid number for quantity")
    else:
        return quantity

def price_validator(price):
    if not (type(price) == int or type(price) == int) and re.match(r"^[0-9.]{5,20}$", price):
        raise ValueError(f"{price} is not a valid number for price")
    else:
        return price
