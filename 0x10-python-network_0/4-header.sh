#!/bin/bash
# send a request with a given header set.
curl -H "X-School-User-Id: 98" "$1" -s;
