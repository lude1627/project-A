import mysql.connector

global conexion
conexion = mysql.connector.connect(
   user = "root",
   password = "",
    host = "localhost",
    database = "project-a",
    port = 3306,
    )
   