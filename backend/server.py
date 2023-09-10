import psycopg2
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='projectpyflask'
                            )
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    users = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', users=users)


# @app.route('/create', methods=('GET', 'POST'))
# def create():
#     if request.method == 'POST':
#         title = request.form['title']
#         first_name = request.form['first_name']
#         last_name = request.form['last_name']
#         active = bool(request.form['active'])
        
#         conn = get_db_connection()
#         cur = conn.cursor()
#         cur.exectue('INSERT INTO users (title, first_name, last_name, active)'
#                     'VALUES (%s, %s, %s, %s)',
#                     (title, first_name, last_name, active))
#         conn.commit()
#         cur.close()
#         conn.close()
# 		return redirect(url_for('index'))
        

# 	return render_template('create.html')


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
        return redirect(url_for('index'))

    return render_template('create.html')
 
if __name__ == '__main__':
    app.run(debug=True)
