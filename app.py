from flask import Flask, jsonify
from flask_migrate import Migrate
from model import db, Movie

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:strongpass@localhost:3306/moviedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/v1/movie/<int:id>')
def get_movie(id):
    # Query the database for the movie information
    movie = Movie.query.get(id)

    # Return a JSON response with the movie information
    if movie is not None:
        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "poster_path": movie.poster_path,
            "language": movie.language,
            "overview": movie.overview,
            "release_date": movie.release_date.strftime('%Y-%m-%d')
        }
        return jsonify(movie_data)
    else:
        return jsonify({'error': 'Movie not found'})

if __name__ == '__main__':
    app.run()
