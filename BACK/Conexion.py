import mysql.connector

def connect():
    conn = mysql.connector.connect(
         host='localhost',
         database='tienda_virtual',
         user='root',
         password='_cindyAPC2005_1#'
     )
    cursor = conn.cursor()
    return conn, cursor

    


