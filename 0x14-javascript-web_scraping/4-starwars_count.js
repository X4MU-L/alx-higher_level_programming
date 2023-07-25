#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, res, body) => {
  let num = 0;
  if (!err) {
    const results = JSON.parse(body).results;
    for (const film of results) {
      if (film.characters.find((usr) => usr === person)) {
        num++;
      }
    }
    console.log(num);
  } else {
    console.log(num);
  }
});
