from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)


conn = psycopg2.connect(database='projectpyflask',
                        user='postgres',
                        password='root',
                        host='localhost',
                        port = '5432'
                        )

cur = conn.cursor()

conn.commit()

cur.close()
conn.close()


@app.route('/')
def index():
    conn = psycopg2.connect(database="projectpyflask",
                            host='localhost',
                            port='5432'
                            )
    
    cur = conn.cursor()
    cur.execute("insert into test_table (column_two) values ('test number 3');")
    data = cur.fetchall()
    cur.close()
    conn.close()
    
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)