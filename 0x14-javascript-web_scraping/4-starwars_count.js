#!/usr/bin/node
const request = require('request');
url = `${process.argv[2]}`;
person = 'https://swapi-api.alx-tools.com/api/people/18/';
request.get(url, (err, res, body) => {
  let results = JSON.parse(body).results;
  num = 0;
  for (let film of results) {
    if (film.charaters.find(usr === url)) {
      num++;
    }
  }
  console.log(num);
});
