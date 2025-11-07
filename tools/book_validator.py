from datetime import datetime
from persiantools.jdatetime import JalaliDateTime


def year_validator(year):
    if not JalaliDateTime.strptime(year, "%Y"):
        raise ValueError("Invalid year format !!!")
    else:
        return year

def tax_validator(tax):
    if  not 0<=tax<=100:
        raise ValueError("Invalid tax number !!!")
    else:
        return tax

def total_discount_validator(total_discount):
    if  not 0<=total_discount<=100:
        raise ValueError("Invalid total discount !!!")
    else:
        return total_discount

def total_amount_validator(total_amount):
    if  not total_amount>=0:
        raise ValueError("Invalid total amount !!!")
    else:
        return total_amount

def isbn_validator(isbn):
    if  not isbn>=0:
        raise ValueError("Invalid isbn amount !!!")
    else:
        return isbn
