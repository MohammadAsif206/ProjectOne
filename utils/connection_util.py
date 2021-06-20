from psycopg2 import connect
from psycopg2._psycopg import OperationalError

import os


def create_connection():
    try:
        con = connect(
            host=os.environ.get('HOST'),
            #host='mohammadasif1.csf3mvrlj6i8.us-west-2.rds.amazonaws.com',
            database=os.environ.get('DB_NAME'),
            #database='postgres',
            user=os.environ.get('DB_USERNAME'),
            #user='asif',
            password=os.environ.get('DB_PASSWORD'),
            #password='Dallas2021206^ws',
            port=os.environ.get('PORT')
            #port='5432'

        )
        return con
    except OperationalError as e:
        print(e)


connection = create_connection()
print(connection)
