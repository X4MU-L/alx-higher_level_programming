#!/usr/bin/node
// create a fucntion that gets the number of occurance of an item

exports.nbOccurences = function (list, searchElement) {
  return (list.filter(n => n === searchElement).length);
};
