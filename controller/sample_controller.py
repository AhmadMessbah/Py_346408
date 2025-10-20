from model import Sample, SampleService

class SampleController:
    def save(self, name, description):
        try:
            sample = Sample(None, name, description)
            print("Ali darkhaste zakhire kard, ok")
            service = SampleService()
            service.save(sample)
            return True, "Saved"
        except Exception as e:
            return False, "Save Error"

    def update(self, sample):
        pass

    def delete(self, id):
        pass

    def find_all(self):
        pass

    def find_by_id(self, id):
        pass
