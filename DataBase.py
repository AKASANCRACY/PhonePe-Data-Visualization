import os
import json
import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Project'
        )

        if connection.is_connected():
            print('Connected to MySQL server')

        database_name = 'PhonePe'

        # Creating a new database
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
        print('Database created successfully')

        # Switching to the new database
        cursor.execute("USE {}".format(database_name))

        # Creating a table to store file information
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS storage (
                id INT AUTO_INCREMENT PRIMARY KEY,
                path VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                content JSON NOT NULL
            )
        ''')
        print('Table created successfully')

    except Error as e:
        print('Error while creating the database', e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection closed')

def store_files(directory_path):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Project',
            database='PhonePe'
        )

        if connection.is_connected():
            print('Connected to MySQL database')

        cursor = connection.cursor()

        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                if file_name.endswith('.json'):
                    file_path = os.path.join(root, file_name)
                    with open(file_path, 'r') as file:
                        file_content = file.read()
                        json_content = json.loads(file_content)

                    cursor.execute("INSERT INTO storage (path, name, content) VALUES (%s, %s, %s)", (file_path, file_name, json.dumps(json_content)))
                    connection.commit()
                    print('File stored successfully:', file_path)

    except Error as e:
        print('Error while storing files', e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            print('Connection closed')

# Specify the directory path where JSON files are located
directory_path = str(os.path.abspath(os.getcwd()))
directory_path = directory_path+'\\temp\data'

def main():
    # Create the new database
    print("From main")
    create_database()
    print(directory_path)
    # Store JSON files in the directory to the database
    store_files(directory_path)
