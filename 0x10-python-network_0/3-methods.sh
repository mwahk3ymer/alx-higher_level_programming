#!/bin/bash
# This script takes a URL as an argument and uses curl to display all HTTP methods the server will accept.
curl -sI -X OPTIONS "$1" | grep -i "allow" | awk '{print $2}'
