#!/bin/bash
# display only status code
curl -I -sw '%{http_code}' "$1" -o /dev/null
