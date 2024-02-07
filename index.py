import sqlite3
path = "./database"
cursor = sqlite3.connect(path)
cursor.execute("SELECT * FROM datable")