#!/bin/bash

# Check if the URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Store the URL in a variable
url=$1

# Use curl to send a request and get the size of the body
response=$(curl -sI "$url")  # Only fetch the headers without the body
size=$(echo "$response" | grep -i "Content-Length" | awk '{print $2}')

# Display the size in bytes
echo "Size of the response body: $size bytes"
