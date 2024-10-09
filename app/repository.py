from typing import List
from app import db
from app.models import Producto

class ProductoRepository:
    def all(self) -> List[Producto]:
        return db.session.query(Producto).all()
    
    def add_product(self, producto: Producto) -> Producto:
        db.session.add(producto)
        db.session.commit()
        return producto
    
    def find_activo(self, id: int) -> Producto:
        if id is None or id == 0:
            return None
        try:
            return db.session.query(Producto).filter(Producto.id == id, Producto.activado == True).one_or_none()
        except:
            return None
