class Employee:
    def __init__(self, id, first_name, last_name, salary, occupation, phone_number, username ,password):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.occupation = occupation
        self.phone_number = phone_number
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.__dict__}"