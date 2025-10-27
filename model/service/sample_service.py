from model import SampleRepository


class SampleService:
    def __init__(self):
        self.repository = SampleRepository()

    def save(self, sample):
        self.repository.save(sample)

    def update(self, sample):
        self.repository.update(sample)

    def delete(self, id):
        self.repository.delete(id)

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, id):
        return self.repository.find_by_id(id)
