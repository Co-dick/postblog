import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="ptanhi",
        database = "blogpost"
    )

    return connection