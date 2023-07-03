#!/bin/bash
# script that takes in a URL, sends a request to that URL
# and displays the size of the body of the response

if [ $# -lt 1 ]
then
    echo "Usage: ${0:2} URL:[port]"
    exit 1
fi

curl "$1"
