import re


def first_name_validator(first_name):
    if not (type(first_name) == str and re.match(r"^\d{1,3}(,\d{3})*$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name


def last_name_validator(last_name):
    if not (type(last_name) == str and re.match(r"^\d{1,3}(,\d{3})*$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name


def salary_validator(salary):
    if not (type(salary) == str and re.match(r"^\d{1,3}(,\d{3})*$", salary)):
        raise ValueError("Invalid first_name !!!")
    else:
        return salary


def phone_number_validator(phone_number):
    if not (type(phone_number) == str and re.match(r"^\d{1,3}(,\d{3})*$", phone_number)):
        raise ValueError("Invalid first_name !!!")
    else:
        return phone_number


def role_validator(role):
    if not (type(role) == str and re.match(r"^[a-zA-Z0-9\s](manager|cashier|storekeeper|sale)$", role)):
        raise ValueError("Invalid role !!!")
    else:
        return role


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
