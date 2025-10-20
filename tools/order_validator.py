import re
from datetime import datetime
from dateutil import parser


def datetime_validator(date_time):
    if not datetime.strptime(date_time, "%Y-%m-%d %H:%M"):
        raise ValueError('Invalid date time format !!!')
    else:
        return date_time

def tax_validator(tax_number):
    if not 0<=tax_number<=100:
        raise ValueError(' Invalid tax number !!!')
    else:
        return tax_number

def total_discount_validator(total_discount):
    if not 0<=total_discount<=100:
        raise ValueError(' Invalid total_discount !!!')
    else:
        return total_discount

def total_amount_validator(total_amount):
    if not total_amount>=0:
        raise ValueError(' Invalid total_amount !!!')
    else:
        return total_amount
