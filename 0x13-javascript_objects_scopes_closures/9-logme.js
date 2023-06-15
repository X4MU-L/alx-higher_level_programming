#!/usr/bin/node
// create a logger fuction

let count = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
