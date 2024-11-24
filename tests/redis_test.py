import os
import unittest
from redis import Redis
from app import create_app, cache, db
from app.models import Producto
from app.services import ProductoService

service = ProductoService()

class RedisTestCase(unittest.TestCase):
    def setUp(self):
        os.environ['FLASK_CONTEXT'] = 'testing'
        self.app = create_app()
        self.app_context = self.app.app_context()
        
        self.app_context.push()
        db.create_all()
        
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    # test connection to Redis
    def test_redis_connection(self):
        redis = Redis(
            host=self.app.config['CACHE_REDIS_HOST'],
            port=self.app.config['CACHE_REDIS_PORT'],
            db=self.app.config['CACHE_REDIS_DB'],
            password=self.app.config['CACHE_REDIS_PASSWORD']
        )
        self.assertTrue(redis.ping())
    
    def test_cache_after_adding_product(self):
        # Simulamos la creación de un producto
        producto = Producto(nombre="Producto Test", precio=123, activado=True)
        producto1 = service.add(producto)
        

        # Verificamos si el producto se guarda correctamente en el cache
        cached_producto = cache.get(f'producto_{producto1.id}')
        
        # Comprobamos que el producto recuperado del cache sea el mismo que guardamos
        self.assertIsNotNone(cached_producto)  # Verificar que no sea None
        self.assertEqual(cached_producto.id, producto1.id)  # Verificar que los IDs coincidan
        self.assertEqual(cached_producto.nombre, producto1.nombre)  # Verificar otros atributos

if __name__ == '__main__':
    unittest.main()