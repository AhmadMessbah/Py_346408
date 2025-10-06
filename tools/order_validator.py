import re
from datetime import datetime

def customer_validator(customer):
    if not (type(customer) == str and re.match(r"^[a-zA-Z\s]{3,30}$", customer)):
        raise ValueError(f"Customer {customer} is not a valid customer name")
    else:
        return customer

def employee_validator(employee):
    if not (type(employee) == str and re.match(r"^[a-zA-Z\s]{3,30}$", employee)):
        raise ValueError(f"Customer {employee} is not a valid customer name")
    else:
        return employee

def order_items_list_validator(order_items_list):
    if  order_items_list is None:
        raise ValueError('order_items_list is None')
    else:
        return order_items_list

def date_validator(date_time):
    if datetime.strptime(date_time, "%Y-%m-%d").date() :
        return date_time
    else:
        raise ValueError('date is invalid!!')

def time_validator(date_time):
    if datetime.strptime(date_time, "%H : %M").time() :
        return date_time
    else:
        raise ValueError('time is invalid!!')


