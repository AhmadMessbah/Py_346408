import re

def document_type_validator(document_type):
    if not (type(document_type) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", document_type)):
        raise ValueError("Invalid document_type !!!")
    else:
        return document_type

def transaction_type_validator(transaction_type):
    if not (type(transaction_type) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", transaction_type)):
        raise ValueError("Invalid transaction_type !!!")
    else:
        return transaction_type

def date_time_validator(date_time):
    if not (type(date_time) == str and re.match(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}$", date_time)):
        raise ValueError("Invalid date_time !!!")
    else:
        return date_time

def customer_id_validator(customer_id):
    if not (type(customer_id) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", customer_id)):
        raise ValueError("Invalid customer_id !!!")
    else:
        return customer_id

def total_amount_validator(total_amount):
    if not (type(total_amount) == str and re.match(r"^\d{1,3}(,\d{3})*$", total_amount)):
        raise ValueError("Invalid total_amount !!!")
    else:
        return total_amount

def items_list_validator(items_list):
    if not (type(items_list) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", items_list)):
        raise ValueError("Invalid items_list !!!")
    else:
        return items_list

def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z0-9\s]*$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description

