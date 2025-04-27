# Flask app
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_anime_list(query=None):
    conn = sqlite3.connect("anime.db")
    cursor = conn.cursor()

    if query:
        cursor.execute("SELECT * FROM anime WHERE LOWER(title) LIKE ?", ('%' + query.lower() + '%',))
    else:
        cursor.execute("SELECT * FROM anime")

    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/', methods=['GET', 'POST'])
def index():
    anime_list = []
    search_query = ""

    if request.method == 'POST':
        search_query = request.form['query']
        anime_list = get_anime_list(search_query)
    else:
        anime_list = get_anime_list()

    return render_template('index.html', anime_list=anime_list, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
