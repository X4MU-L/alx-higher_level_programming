#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
const person = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, res, body) => {
  if (!err) {
    let num = 0;
    for (const film of JSON.parse(body).results) {
      if (film.characters.find((usr) => usr === person)) {
        num++;
      }
    }
    console.log(num);
    return;
  }
  console.log(0);
});
