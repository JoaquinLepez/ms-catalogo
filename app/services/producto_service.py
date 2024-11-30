from ..repository import ProductoRepository
from app.models import Producto
from app import cache

repository = ProductoRepository()

class ProductoService:

    def all(self) -> list[Producto]:
        result = cache.get('productos')
        if result is None:
            result = repository.all()
            cache.set('productos', result, timeout=15)
        return result
    
    def add(self, producto: Producto) -> Producto:
        producto = repository.add_product(producto)
        cache.set(f'producto_{producto.id}', producto, timeout=15)
        return producto
    
    def find_activo(self, id: int) -> Producto:
        result = repository.find_activo(id)    
        return result 

