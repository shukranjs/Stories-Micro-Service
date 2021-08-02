import os
import redis

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flasgger import Swagger

from ..app import app

BASE_DIRS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_ROOT = os.path.join(BASE_DIRS, 'media')


class RedisConfig:
    HOST = os.environ.get('REDIS_HOST', 'localhost')
    PORT = os.environ.get('REDIS_PORT', 6379)
    CHANNEL_NAME = 'events'
    PASSWORD = os.environ.get('REDIS_PASSWORD', '1234')

    @property
    def client(self):
        return redis.Redis(host=self.HOST, port=self.PORT, password=self.PASSWORD, db=0)


app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://db_user:123@127.0.0.1:5432/db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
ma = Marshmallow(app)
swagger = Swagger(app)
