#!/bin/bash

# Check if the URL argument is provided
curl -sI "$url" | wc -c
