#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Retrieve command-line arguments
    username, password, database_name = argv[1], argv[2], argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database_name)

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows from the result set
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
