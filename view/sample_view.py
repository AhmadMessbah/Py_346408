# View
from controller.sample_controller import SampleController

name = input("Enter name : ")
description = input("Enter description : ")

sample_controller = SampleController()
sample_controller.save(name, description)

