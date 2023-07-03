#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl "$1" -s | tee | wc -c;
