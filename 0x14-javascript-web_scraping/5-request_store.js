#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  err && console.log(err);
  fs.writeFileSync(process.argv[3], body, 'utf-8');
});
