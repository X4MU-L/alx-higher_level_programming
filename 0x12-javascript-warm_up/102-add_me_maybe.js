#!/usr/bin/node
// create a function thatincrements its first argument

exports.addMeMaybe = (num, func) => {
  num++;
  func(num);
};
