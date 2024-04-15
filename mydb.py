# install mysql
#install mysql-connector
#install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Admin123!' 


	)

#prepare a cursor object 
cursorObject = dataBase.cursor()


#create a database 
cursorObject.execute("CREATE DATABASE vendordb")

print("All done!")