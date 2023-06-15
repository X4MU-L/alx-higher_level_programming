#!/usr/bin/node
// import and sort a dictionary

const dict = require('./101-data.js').dict;

const newDict = {};

for (const obj in dict) {
  if (newDict[dict[obj]]) {
    newDict[dict[obj]].push(obj);
  } else {
    newDict[dict[obj]] = [obj];
  }
}

console.log(newDict);
