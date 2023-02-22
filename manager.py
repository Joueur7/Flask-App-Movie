from flask import Flask
from flask_migrate import Migrate
from models.movie_model import db
from controllers.movie_controller import movies_controller

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:strongpass@localhost:3306/moviedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(movies_controller)

if __name__ == '__main__':
    app.run()
