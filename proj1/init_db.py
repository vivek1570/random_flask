import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('First Post', 'Content for the first post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Third Post', 'Content for the third post')
#             )

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Fourth Post', 'Content fourth the third post')
#             )

# cur.execute("INSERT INTO info (peru, phone, addr) VALUES (?, ?, ?)",
#             ('Vivek',9946002888,'123 main street')
            # )

connection.commit()
connection.close()