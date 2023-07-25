#!/usr/bin/node
const request = require('request');
const url = `${process.argv[2]}`;
request.get(url, (err, res, body) => {
  err && console.log(err);
  const obj = {};
  const todos = JSON.parse(body);
  for (const todo of todos) {
    if (obj[todo.userId] && todo.completed) {
      obj[todo.userId]++;
    } else if (!obj[todo.userId] && todo.completed) {
      obj[todo.userId] = 1;
    }
  }
  console.log(obj);
});
