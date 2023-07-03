#!/bin/bash
# send a post request using a json file
curl -X POST -H "Content-Type: application/json" -d @"$2" "$1";
