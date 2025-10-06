class Bank:
    def __init__(self, id, name, account, balance, description):
        self.id = id
        self.name = name
        self.account = account
        self.balance = balance
        self.description = description

    def __repr__(self):
        return f"{self.__dict__}"
