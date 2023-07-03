#!/bin/bash
# send a post request using a json file
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1";
