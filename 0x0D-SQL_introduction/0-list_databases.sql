import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
	    host="your_host",
	    user="your_username",
	    password="your_password"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Execute the SQL query to list all databases
cursor.execute("SHOW DATABASES")

# Fetch all database names and print them
databases = cursor.fetchall()
for db in databases:
	    print(db[0])

# Close the cursor and the database connection
cursor.close()
connection.close()
