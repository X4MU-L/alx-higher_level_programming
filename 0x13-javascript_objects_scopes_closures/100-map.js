#!/usr/bin/node
// import and map a list

const list = require('./100-data').list;

const newList = list.map((item, i) => item * i);
console.log(list);
console.log(newList);
