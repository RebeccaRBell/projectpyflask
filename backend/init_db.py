import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="projectpyflask"
        )
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD'])

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'title varchar (10) NOT NULL,'
                                 'first_name varchar (50) NOT NULL,'
                                 'last_name varchar(50) NOT NULL,'
                                 'active boolean NOT NULL,'
                                 'date_created date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the table

cur.execute('INSERT INTO users (title, first_name, last_name, active)'
            'VALUES (%s, %s, %s, %s)',
            ('Mr',
             'Lewis',
             'Halstead',
             True)
            )


cur.execute('INSERT INTO users (title, first_name, last_name, active)'
            'VALUES (%s, %s, %s, %s)',
            ('Ms',
             'Becca',
             'Bell',
             False)
            )

conn.commit()

cur.close()
conn.close()