#!/usr/bin/node
// create a fuction that reverses a list without reverse


exports.esrever = function (list) {
    let l = list.length;
    return (list.map((item) => list[--l]));
}
