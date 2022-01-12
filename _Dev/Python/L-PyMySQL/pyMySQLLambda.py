
# https://www.youtube.com/watch?v=vyLvmPkQZkI
# pip install -t $PWD pymysql

# import pymysql

# 1. Install pymysql to local directory
# pip install -t $PWD pymysql

# 2. (If Using Lambda) Write your code, then zip it all up 
# a) Mac/Linux --> zip -r9 ${PWD}/function.zip 
# b) Windows --> Via Windows Explorer

# Lambda Permissions:
# AWSLambdaVPCAccessExecutionRole

#Configuration Values
endpoint = 'yourendpoint.com'
username = 'your username'
password = 'your password'
database_name = 'your database name'

#Connection
connection = pymysql.connect(endpoint, user=username,
	passwd=password, db=database_name)

def lambda_handler(event, context):
	cursor = connection.cursor()
	cursor.execute('SELECT * from Transactions')

	rows = cursor.fetchall()

	for row in rows:
		print("{0} {1} {2}".format(row[0], row[1], row[2]))