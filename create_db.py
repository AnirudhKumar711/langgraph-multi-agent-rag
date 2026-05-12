import sqlite3

conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")

cursor.execute("""
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    title TEXT,
    country TEXT,
    genre TEXT,
    rating REAL
)
""")

movies = [

# --- USA ---
("Inception", "USA", "Sci-Fi", 4.8),
("Interstellar", "USA", "Sci-Fi", 4.7),
("The Dark Knight", "USA", "Action", 4.9),
("Avengers: Endgame", "USA", "Action", 4.6),
("Titanic", "USA", "Romance", 4.5),
("Gladiator", "USA", "Action", 4.6),
("The Matrix", "USA", "Sci-Fi", 4.7),
("Fight Club", "USA", "Drama", 4.8),
("Forrest Gump", "USA", "Drama", 4.9),
("Joker", "USA", "Drama", 4.6),
("Batman Begins", "USA", "Action", 4.5),
("Iron Man", "USA", "Action", 4.4),
("Thor", "USA", "Action", 4.2),
("Captain America", "USA", "Action", 4.3),
("Doctor Strange", "USA", "Sci-Fi", 4.5),
("Black Panther", "USA", "Action", 4.6),
("Spider-Man: No Way Home", "USA", "Action", 4.7),
("Deadpool", "USA", "Comedy", 4.5),
("The Lion King", "USA", "Animation", 4.8),
("Frozen", "USA", "Animation", 4.4),

# --- INDIA ---
("RRR", "India", "Action", 4.7),
("Dangal", "India", "Drama", 4.8),
("3 Idiots", "India", "Comedy", 4.9),
("Baahubali: The Beginning", "India", "Action", 4.6),
("Baahubali: The Conclusion", "India", "Action", 4.8),
("KGF Chapter 1", "India", "Action", 4.5),
("KGF Chapter 2", "India", "Action", 4.6),
("Pushpa", "India", "Action", 4.4),
("Drishyam", "India", "Thriller", 4.7),
("Andhadhun", "India", "Thriller", 4.8),
("Lagaan", "India", "Drama", 4.7),
("Swades", "India", "Drama", 4.6),
("PK", "India", "Comedy", 4.5),
("Chhichhore", "India", "Drama", 4.6),
("Zindagi Na Milegi Dobara", "India", "Drama", 4.5),
("Barfi", "India", "Romance", 4.6),
("Rockstar", "India", "Drama", 4.5),
("Queen", "India", "Drama", 4.6),
("Gully Boy", "India", "Drama", 4.4),
("Taare Zameen Par", "India", "Drama", 4.9),

# --- KOREA ---
("Parasite", "Korea", "Thriller", 4.8),
("Train to Busan", "Korea", "Action", 4.6),
("Oldboy", "Korea", "Thriller", 4.7),
("Memories of Murder", "Korea", "Thriller", 4.8),
("The Host", "Korea", "Sci-Fi", 4.5),
("Snowpiercer", "Korea", "Sci-Fi", 4.4),
("The Wailing", "Korea", "Horror", 4.5),
("Burning", "Korea", "Drama", 4.4),
("A Taxi Driver", "Korea", "Drama", 4.6),
("The Chaser", "Korea", "Thriller", 4.5),

# --- JAPAN ---
("Spirited Away", "Japan", "Animation", 4.9),
("Your Name", "Japan", "Romance", 4.8),
("Weathering With You", "Japan", "Romance", 4.6),
("Akira", "Japan", "Sci-Fi", 4.7),
("Grave of the Fireflies", "Japan", "Drama", 4.9),
("Princess Mononoke", "Japan", "Animation", 4.8),
("Howl's Moving Castle", "Japan", "Animation", 4.7),
("Tokyo Drift", "Japan", "Action", 4.3),
("Battle Royale", "Japan", "Thriller", 4.5),
("Ringu", "Japan", "Horror", 4.4),

# --- UK ---
("Harry Potter 1", "UK", "Fantasy", 4.6),
("Harry Potter 2", "UK", "Fantasy", 4.5),
("Harry Potter 3", "UK", "Fantasy", 4.7),
("Harry Potter 4", "UK", "Fantasy", 4.5),
("Harry Potter 5", "UK", "Fantasy", 4.4),
("Harry Potter 6", "UK", "Fantasy", 4.5),
("Harry Potter 7", "UK", "Fantasy", 4.7),
("James Bond: Skyfall", "UK", "Action", 4.6),
("Sherlock Holmes", "UK", "Mystery", 4.5),
("The King's Speech", "UK", "Drama", 4.6),

# --- EXTRA MIX ---
("Avatar", "USA", "Sci-Fi", 4.6),
("Avatar: The Way of Water", "USA", "Sci-Fi", 4.5),
("The Godfather", "USA", "Crime", 4.9),
("The Shawshank Redemption", "USA", "Drama", 5.0),
("Pulp Fiction", "USA", "Crime", 4.8),
("Se7en", "USA", "Thriller", 4.7),
("Whiplash", "USA", "Drama", 4.8),
("La La Land", "USA", "Romance", 4.6),
("The Prestige", "USA", "Drama", 4.7),
("Memento", "USA", "Thriller", 4.7),

("Dil Chahta Hai", "India", "Drama", 4.6),
("Kabir Singh", "India", "Drama", 4.2),
("Shershaah", "India", "War", 4.6),
("Article 15", "India", "Drama", 4.5),
("Special 26", "India", "Crime", 4.4),

("I Saw the Devil", "Korea", "Thriller", 4.6),
("Decision to Leave", "Korea", "Romance", 4.4),

("One Piece Film Red", "Japan", "Animation", 4.3),
("Suzume", "Japan", "Animation", 4.5)
]

cursor.executemany("""
INSERT INTO movies (title, country, genre, rating)
VALUES (?, ?, ?, ?)
""", movies)

conn.commit()
conn.close()

print("✅ Database created with", len(movies), "movies")