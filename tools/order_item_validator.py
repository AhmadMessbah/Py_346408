import re

def quantity_validator(quantity):
    if not (type(quantity) == int and re.match(r"^[0-9]{5,20}$", quantity)):
        raise ValueError("Invalid quantity !!!")
    else:
        return quantity

def price_validator(price):
    if not (type(price) == int or type(price) == float) and re.match(r"^[0-9.]{5,20}$", price):
        raise ValueError("Invalid price !!!")
    else:
        return price

def discount_validator(total_discount):
    if not 0 <= total_discount <= 100:
        raise ValueError(' Invalid total_discount !!!')
    else:
        return total_discount

def description_validator(description):
    if not type(description) == str  and re.match(r"^[a-zA-Z]{10,30}$", description):
        raise ValueError("Invalid description !!!")
    else:
        return description
