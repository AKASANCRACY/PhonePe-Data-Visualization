import mysql.connector
from mysql.connector import Error
import pandas as pd
import os

def GetData(data,year,month,Path):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Project',
            database='PhonePe'
        )

        if connection.is_connected():
            print('Connected to MySQL database')

        path = str(os.path.abspath(os.getcwd()))
        path = path+"\\temp\data"
        cursor = connection.cursor()
        if Path=="A":
            path = path+"\\aggregated\\" + data.lower() + "\country\india\\" + year + "\\" + month[1] + ".json"
        elif Path=="M":
            path = path+"\map\\" + data.lower() + "\hover\country\india\\" + year + "\\" + month[1] + ".json"
        elif Path=="T":
            path = path+"\\top\\" + data.lower() + "\country\india\\" + year + "\\" + month[1] + ".json"
        print(path)
        sql = ("SELECT content FROM storage WHERE path = %s")
        val =(path, )
        cursor.execute(sql,val)

        rows = cursor.fetchall()
        return rows[0][0]
        
    except Error as e:
        return 0

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
