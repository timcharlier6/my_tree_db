import csv
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('my_trees.db')
cursor = conn.cursor()

# Open the CSV file
with open('my_trees.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    headers = next(csv_reader)  # Skip the header row

    # Insert each row into the table
    for row in csv_reader:
        cursor.execute('''
        INSERT INTO my_trees (espece, variete, nom_francais, zone, pepiniere, taille, bouture, hauteur, nbre, gout)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', row)

# Commit the changes and close the connection
conn.commit()
conn.close()
