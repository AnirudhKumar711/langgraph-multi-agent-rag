import sqlite3

# --- Map common words → DB values ---
COUNTRY_MAP = {
    "india": "India",
    "usa": "USA",
    "us": "USA",
    "japan": "Japan",
    "korea": "Korea",
    "uk": "UK",
    "britain": "UK",
}

GENRE_MAP = {
    "action": "Action",
    "superhero": "Action",   # map superhero → Action
    "comedy": "Comedy",
    "romance": "Romance",
    "sci-fi": "Sci-Fi",
    "science fiction": "Sci-Fi",
    "thriller": "Thriller",
    "drama": "Drama",
    "animation": "Animation",
    "fantasy": "Fantasy",
    "crime": "Crime",
    "horror": "Horror",
    "war": "War",
    "mystery": "Mystery",
}

def generate_sql(query: str) -> str:
    q = query.lower()

    conditions = []

    # --- detect country ---
    for key, value in COUNTRY_MAP.items():
        if key in q:
            conditions.append(f"country='{value}'")
            break  # only one country needed

    # --- detect genre ---
    for key, value in GENRE_MAP.items():
        if key in q:
            conditions.append(f"genre='{value}'")
            break  # only one genre needed

    base_query = "SELECT title, genre, rating FROM movies"

    # --- apply filters ---
    if conditions:
        base_query += " WHERE " + " AND ".join(conditions)

    # --- sorting ---
    if "top" in q or "best" in q or "highest" in q:
        base_query += " ORDER BY rating DESC LIMIT 5"

    return base_query + ";"


def run_sql(sql: str):
    conn = sqlite3.connect("movies.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    results = cursor.fetchall()
    conn.close()
    return results


def sql_agent(state):
    query = state["query"]

    sql = generate_sql(query)
    result = run_sql(sql)

    return {"result": result}