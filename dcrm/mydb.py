import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password',
    auth_plugin = 'mysql_native_password'
)

cursorObject = database.cursor()

# create database

cursorObject.execute("CREATE DATABASE elderco")

print("ALL DONE !")