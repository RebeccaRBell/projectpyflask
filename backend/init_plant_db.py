import os
import psycopg2

conn = psycopg2.connect(
        host="localhost",
        database="projectpyflask"
        )

cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS plants;')

cur.execute('CREATE TABLE plants (id serial PRIMARY KEY,'
            'plant_id varchar(255),'
            'common_name varchar(255),'
            'scientific_name varchar(255),'
            'family varchar(255),'
            'description varchar(255),'
            'care_instructions varchar(255),'
            'image_url varchar(255),'
            'created_on date DEFAULT CURRENT_TIMESTAMP,'
            'updated_on date DEFAULT CURRENT_TIMESTAMP);'
            )

cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))

cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))
cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))
cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))
cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))
cur.execute('INSERT INTO plants (plant_id, common_name, scientific_name, family, description, care_instructions)'
            'VALUES (%s, %s, %s, %s, %s, %s)',
            ('1',
             'Snake Plant',
             'Sansevieria Trifasciata',
             'Asparagaceae',
             "Snake Plant, also known as the Mother-in-law's Tongue, is a popular and hardy indoor plant. It is known for its striking upright leaves with green and yellow stripes.",
             'Snake Plants are low-maintenance and thrive in indirect light. Water sparingly and allow the soil to dry between waterings.'
             ))

conn.commit()

cur.close()
conn.close()
