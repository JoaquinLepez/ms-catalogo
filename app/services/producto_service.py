from ..repository import ProductoRepository
from app.models import Producto

repository = ProductoRepository()

class ProductoService:

    def all(self) -> list[Producto]:
        return repository.all()
    
    def add(self, producto: Producto) -> Producto:
        return repository.add_product(producto)
    
    def find_activo(self, id: int) -> Producto:
        return repository.find_activo(id)

