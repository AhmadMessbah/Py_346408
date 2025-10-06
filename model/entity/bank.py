class Bank:
    def __init__(self,balance, id, name, account, description, bank_number=None):
        self.balance = balance
        self.id = id
        self.name = name
        self.account = account
        self.description = description


    def __repr__(self):
        return f"{self.__dict__}"