#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me using curl to trigger the server response.
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me
