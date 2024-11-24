from ..repository import ProductoRepository
from app.models import Producto
from app import cache

repository = ProductoRepository()

class ProductoService:

    def all(self) -> list[Producto]:
        result = cache.get('roles')
        if result is None:
            result = repository.all()
            cache.set('roles', result, timeout=15)
        return result
    
    def add(self, producto: Producto) -> Producto:
        producto = repository.add_product(producto)
        cache.set(f'producto_{producto.id}', producto, timeout=15)
        return producto
    
    def find_activo(self, id: int) -> Producto:
        result = cache.get(f'role_{id}')
        if result is None:
            result = repository.find_activo(id)
            cache.set(f'role_{id}', result, timeout=15)
        
        return result 

