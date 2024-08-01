import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('my_trees.db')
cursor = conn.cursor()

# Create table schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS my_trees (
    espece TEXT,
    variete TEXT,
    nom_francais TEXT,
    zone INTEGER,
    pepiniere TEXT,
    taille TEXT,
    bouture TEXT,
    hauteur TEXT,
    nbre INTEGER,
    gout TEXT
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

