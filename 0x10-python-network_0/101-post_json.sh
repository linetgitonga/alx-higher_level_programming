#!/bin/bash
# sends a JSON POST request to a URL passed as the argument 
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
