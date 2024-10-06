import unittest, os
from app import create_app, db
from app.models import Producto
class UserTestCase(unittest.TestCase):
    
    def setUp(self):
        # User
        self.NOMBRE_PRUEBA = 'lampara'
        self.PRECIO_PRUEBA = 456542
        self.ACTIVADO_PRUEBA = True
    
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    def test_user(self):
        
        producto = self.__get_producto()
        # db.session.add(user)
        # db.session.commit()
        self.assertEqual(producto.nombre, self.NOMBRE_PRUEBA)
        self.assertEqual(producto.precio, self.PRECIO_PRUEBA)
        self.assertEqual(producto.activado, self.ACTIVADO_PRUEBA)
    

    def __get_producto(self):
        producto = Producto()
        producto.nombre = self.NOMBRE_PRUEBA
        producto.precio = self.PRECIO_PRUEBA
        producto.activado = self.ACTIVADO_PRUEBA

        return producto
    
if __name__ == '__main__':
    unittest.main()