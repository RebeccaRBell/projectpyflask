import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="projectpyflask"
        )

cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS users;')
cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
                                 'title varchar (10) NOT NULL,'
                                 'first_name varchar (50) NOT NULL,'
                                 'last_name varchar(50) NOT NULL,'
                                 'password varchar(20) NOT NULL,'
                                 'active boolean NOT NULL,'
                                 'date_created date DEFAULT CURRENT_TIMESTAMP);'
                                 )


cur.execute('INSERT INTO users (title, first_name, last_name, password, active)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('X',
             'Admin',
             'User',
             'P4ssW0rd',
             False)
            )

cur.execute('INSERT INTO users (title, first_name, last_name, password, active)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Mr',
             'Lewis',
             'Halstead',
             'Password123',
             True)
            )

cur.execute('INSERT INTO users (title, first_name, last_name, password, active)'
            'VALUES (%s, %s, %s, %s, %s)',
            ('Ms',
             'Becca',
             'Bell',
             'Password321',
             False)
            )


conn.commit()

cur.close()
conn.close()