#!/bin/bash

# This script lists all databases on a MySQL server

# MySQL username and password
MYSQL_USER="your_username"
MYSQL_PASSWORD="your_password"

# Use the mysql command to execute the query
mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -e "SHOW DATABASES;"
