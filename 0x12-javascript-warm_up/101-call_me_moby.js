#!/usr/bin/node
// create a function that adds two integers

exports.callMeMoby = (num, func) => {
    while (num > 0) {
	func();
	num--;
    }
};
