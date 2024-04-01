#!/bin/bash
# sends a request to a URL passed as an argumentthen displays only the status code of the response
curl -so /dev/null --write-out "%{http_code}" "$1"
