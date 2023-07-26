#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  if (!err) {
    const obj = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        if (obj[todo.userId]) {
          obj[todo.userId]++;
        } else {
          obj[todo.userId] = 1;
        }
      }
    }
    console.log(obj);
  }
});
