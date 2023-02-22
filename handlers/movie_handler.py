from models.movie_model import Movie

def get_movie_handler(id):
    # Query the database for the movie information
    movie = Movie.query.get(id)

    # Return a dictionary with the movie information
    if movie is not None:
        movie_data = {
            "id": movie.id,
            "title": movie.title,
            "poster_path": movie.poster_path,
            "language": movie.language,
            "overview": movie.overview,
            "release_date": movie.release_date.strftime('%Y-%m-%d')
        }
        return movie_data
    else:
        return {'error': 'Movie not found'}
