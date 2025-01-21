from ..repository import ProductoRepository
from app.models import Producto

repository = ProductoRepository()

class ProductoService:

    def all(self) -> list[Producto]:
        result = repository.all()
        return result
    
    def add(self, producto: Producto) -> Producto:
        producto = repository.add_product(producto)
        return producto
    
    def find_activo(self, id: int) -> Producto:
        result = repository.find_activo(id)    
        return result 

