from flask import Flask
from flask_migrate import Migrate
from models.movie_model import db
from controllers.movie_controller import movies_controller
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)
user = os.getenv('DB_USER')
password = os.getenv('DB_PASS')
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
name = os.getenv('DB_NAME')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
    user,
    password,
    host,
    port,
    name
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(movies_controller)

if __name__ == '__main__':
    app.run()
