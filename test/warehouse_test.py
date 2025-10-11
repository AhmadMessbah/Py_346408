from model.entity.warehouse import Warehouse
from model.service.warehouse_service import WarehouseService


warehouse = Warehouse(None, 123, 2)

warehouse_service = WarehouseService()
warehouse_service.save(warehouse)
warehouse_service.update(warehouse)
warehouse_service.delete(id)
print(warehouse_service.find_all())
print(warehouse_service.find_by_id(id))




