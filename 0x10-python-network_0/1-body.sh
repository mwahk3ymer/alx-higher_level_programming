#!/bin/bash
# This script takes a URL as an argument, sends a GET request using curl, and displays the body of the response for a 200 status code.
curl -s -X GET "$1" -w "%{http_code}" | awk 'END {if ($1 == "200") print $0}'
