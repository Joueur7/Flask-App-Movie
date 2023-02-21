# Flask-App-Movie

# First Step to migrate
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# To add movie to SQL database
movie = Movie(
    title='The Lord of the Rings: The Fellowship of the Ring',
    poster_path='https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
    language='English',
    overview='A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron, begins his journey with eight companions to Mount Doom, the only place where it can be destroyed.',
    release_date=datetime(2001, 12, 19)
)
db.session.add(movie)
db.session.commit()
