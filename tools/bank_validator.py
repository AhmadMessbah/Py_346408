import re


def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name)):
        raise ValueError("Invalid Name !!!")
    else:
        return name

def account_validator(account):
    if not (type(account) == str and re.match(r"^\d{1,3}(,\d{3})*$", account)):
        raise ValueError("Invalid salary !!!")
    else:
        return account
def balance_validator(balance):
    if not (type(balance) == int and re.match(r"^[0-9]{5,20}$", balance)):
        raise ValueError(f"{balance} is not a valid number for quantity")
    else:
        return balance


def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description