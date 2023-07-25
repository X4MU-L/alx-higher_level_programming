#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (body) {
    fs.writeFile(
      process.argv[3],
      body,
      'utf-8',
      (err) => err && console.log(err)
    );
  } else {
    console.log(err);
  }
});
