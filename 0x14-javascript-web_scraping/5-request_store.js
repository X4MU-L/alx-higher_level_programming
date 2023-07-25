#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (body) {
    fs.writeFile(process.argv[3], 'utf-8', (err, data) => console.log(err));
  } else {
    console.log(err);
  }
});
