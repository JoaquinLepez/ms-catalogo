from app import db
class Producto(db.Model):
    __tablename__ = 'productos'
    # Atributos propios
    id: int = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nombre: str = db.Column(db.String(80), nullable = False)
    precio: str = db.Column(db.Float, nullable = False)
    activado: bool = db.Column(db.Boolean, nullable = False)

