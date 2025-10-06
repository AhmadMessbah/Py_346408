from model.entity.sample import Sample
from model.service.sample_service import SampleService

sample = Sample(None, "Ali", "Tozihat")

sample_service = SampleService()
sample_service.save(sample)
sample_service.update(sample)
sample_service.delete(id)
print(sample_service.find_all())
print(sample_service.find_by_id(id))

