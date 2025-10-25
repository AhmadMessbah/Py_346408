from model import SampleRepository


class SampleService:
    def __init__(self):
        self.repository = SampleRepository()

    def save(self, sample):
        return self.repository.save(sample)

    def update(self, sample):
        sample_result = self.repository.find_by_id(sample.id)
        if sample_result:
            self.repository.update(sample)
            return sample
        else:
            raise Exception("Sample Not Found !!!")

    def delete(self, sample_id):
        sample = self.repository.find_by_id(sample_id)
        if sample:
            self.repository.delete(sample_id)
            return sample
        else:
            raise Exception("Sample Not Found !!!")

    def find_all(self):
        return self.repository.find_all()

    def find_by_id(self, sample_id):
        sample = self.repository.find_by_id(sample_id)
        if sample:
            return sample
        else:
            raise Exception("Sample Not Found !!!")
