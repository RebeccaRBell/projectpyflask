import psycopg2
from psycopg2 import extras
from flask import Flask, render_template, request, url_for, redirect, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='projectpyflask')
    return conn


@app.route('/api/users')
def users_api():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users

@app.route('/api/plants')
def plant_api():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=extras.DictCursor)
    cur.execute('SELECT * FROM plants;')
    plants = cur.fetchall()
    cur.close()
    conn.close()

    plant_list = []
    for plant in plants:
        plant_dict = {
            "name": plant["common_name"],
            "scientific_name": plant["scientific_name"],
            "family": plant["family"],
            "description": plant["description"],
            "care_instructions": plant["care_instructions"]
        }
        plant_list.append(plant_dict)

    return jsonify(plant_list)


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users FETCH FIRST 1 ROWS ONLY;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('login.html')


@app.route('/home')
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('home.html', users=users)


@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        try: 
            active = bool(request.form['active'])
        except:
            active = False

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (title, first_name, last_name, active)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, first_name, last_name, active))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('create'))

    return render_template('create.html')


@app.route('/edit/<int:id>/', methods=('GET', 'POST'))
def edit(id):
    if request.method == 'POST':
        title = request.form['title']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        try:
            active = bool(request.form['active'])
        except:
            active = False
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE users SET title=%s, first_name=%s, last_name=%s, active=%s WHERE id=%s',
                    (title, first_name, last_name, active, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('home'))
    
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('edit.html', user=users[id], id=id)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
 
if __name__ == '__main__':
    app.run(debug=True)


