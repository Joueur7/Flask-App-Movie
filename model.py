from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# Define the movies table
class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    poster_path = db.Column(db.String(255), nullable=False)
    language = db.Column(db.String(50), nullable=False)
    overview = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Movie {self.id}>'
