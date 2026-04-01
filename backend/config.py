class Settings:
    def __init__(self):
        self.database = {
            'engine': 'django.db.backends.postgresql',
            'name': 'your_db_name',
            'user': 'your_db_user',
            'password': 'your_db_password',
            'host': 'localhost',
            'port': '5432',
        }
        self.mqtt = {
            'broker': 'mqtt.example.com',
            'port': 1883,
            'username': 'your_mqtt_user',
            'password': 'your_mqtt_password',
        }
        self.jwt = {
            'secret': 'your_jwt_secret',
            'algorithm': 'HS256',
            'expiration_time': 3600,
        }
        self.app = {
            'debug': True,
            'port': 5000,
            'host': '0.0.0.0',
        }
