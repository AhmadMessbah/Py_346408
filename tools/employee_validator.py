import re

def salary_validator(salary):
    if not (type(salary) == str and re.match(r"^\d{1,3}(,\d{3})*$", salary)):
        raise ValueError("Invalid salary !!!")
    else:
        return salary

def occupation_validator(occupation):
    if not (type(occupation) == str and re.match(r"^[a-zA-Z0-9\s](manager|cashier|storekeeper|sale)$", occupation)):
        raise ValueError("Invalid occupation !!!")
    else:
        return occupation

def username_validator(username):
    if not (type(username) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", username)):
        raise ValueError("Invalid username !!!")
    else:
        return username
def password_validator(password):
    if not (type(password) == str and re.match(r"^[a-zA-Z0-9\s][.\w]{3,30}(@|&)$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password

