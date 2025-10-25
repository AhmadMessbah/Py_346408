from model import Sample, SampleService
from tools.logging import Logger


class SampleController:
    sample_service = SampleService()

    @classmethod
    def save(cls, name, description):
        try:
            sample = Sample(None, name, description)
            sample = cls.sample_service.save(sample)
            Logger.info(f"Sample {sample} saved")
            return True, f"Sample Saved Successfully"
        except Exception as e:
            Logger.error(f"Sample Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, sample_id, name, description):
        try:
            sample = Sample(sample_id, name, description)
            sample = cls.sample_service.update(sample)
            Logger.info(f"Sample {sample} updated")
            return True, "Sample Updated Successfully"
        except Exception as e:
            Logger.error(f"Sample Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, sample_id):
        try:
            sample = cls.sample_service.delete(sample_id)
            Logger.info(f"Sample {sample} deleted")
            return True, f"Sample Deleted Successfully"
        except Exception as e:
            Logger.error(f"Sample Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            sample_list = cls.sample_service.find_all()
            Logger.info("Sample FindAll")
            return True, sample_list
        except Exception as e:
            Logger.error(f"Sample FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, sample_id):
        try:
            sample = cls.sample_service.find_by_id(sample_id)
            Logger.info(f"Sample FindById {sample_id}")
            return True, sample
        except Exception as e:
            Logger.error(f"Sample FindById Error: {e}")
            return False, e
