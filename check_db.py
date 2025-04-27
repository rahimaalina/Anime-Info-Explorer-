import sqlite3

conn = sqlite3.connect("anime.db")
cursor = conn.cursor()

try:
    cursor.execute("SELECT * FROM anime")
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("⚠️ No anime data found in anime.db!")
except sqlite3.Error as e:
    print(f"Database error: {e}")

conn.close()
 
