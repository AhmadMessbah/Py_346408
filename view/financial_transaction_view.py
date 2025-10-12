# View
from controller.bank_controller import BankController

name = input("Enter name : ")
account = input("Enter account number : ")
balance = input("Enter balance : ")
description = input("Enter description : ")

bank_controller = BankController()
bank_controller.save(name,balance ,account,description)
