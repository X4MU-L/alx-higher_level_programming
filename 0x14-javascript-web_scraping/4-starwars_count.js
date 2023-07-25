#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, res, body) => {
  err && console.log(err);
  let num = 0;
  for (const film of JSON.parse(body).results) {
    if (film.characters.find((usr) => usr === person)) {
      num++;
    }
  }
  console.log(num);
});
