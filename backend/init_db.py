import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="projectpyflask"
        )

cur = conn.cursor()


cur.execute('DROP TABLE IF EXISTS users;')

cur.execute('CREATE TABLE users (id serial PRIMARY KEY,'
            'title varchar(10) NOT NULL,'
            'first_name varchar(50) NOT NULL,'
            'email varchar(100),'
            'last_name varchar(50) NOT NULL,'
            'username varchar(50),'
            'password varchar(20),'
            'active boolean NOT NULL,'
            'date_created date DEFAULT CURRENT_TIMESTAMP);'
            )

cur.execute('''
    CREATE OR REPLACE FUNCTION generate_username(first_name VARCHAR, last_name VARCHAR) RETURNS VARCHAR AS $$
    DECLARE
        base_username VARCHAR;
        unique_username VARCHAR;
    BEGIN
        -- Concatenate the first letter of the first name with the last name
        base_username := SUBSTRING(first_name, 1, 1) || last_name;

        -- Generate a unique username by appending a number
        SELECT base_username || COALESCE(MAX(substring(username, LENGTH(base_username) + 1)::INT) + 1, '1')
        INTO unique_username
        FROM users
        WHERE username LIKE base_username || '%';

        RETURN unique_username;
    END;
    $$ LANGUAGE plpgsql;
''')

cur.execute('''
    CREATE OR REPLACE FUNCTION generate_username_trigger() RETURNS TRIGGER AS $$
    BEGIN
        IF NEW.username IS NULL THEN
            NEW.username := generate_username(NEW.first_name, NEW.last_name);
        END IF;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;

    CREATE TRIGGER before_insert_generate_username
    BEFORE INSERT ON users
    FOR EACH ROW
    EXECUTE FUNCTION generate_username_trigger();
''')


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
