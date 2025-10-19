from model.entity.warehouse_transaction import WarehouseTransaction
from model.service.warehouse_service import WarehouseService

warehouse_transaction = WarehouseTransaction(1,12,3,"output",None,122,455)
service = WarehouseService()
#service.save(warehouse_transaction)
#service.update(warehouse_transaction)
#print(service.find_all())
#print(service.find_by_id(1))
#service.delete(1)

