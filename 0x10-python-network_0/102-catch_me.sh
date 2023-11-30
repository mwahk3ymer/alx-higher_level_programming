#!/bin/bash
# This script makes a request to 0.0.0.0:5000/catch_me causing the server to respond with "You got me!" in the body.
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
