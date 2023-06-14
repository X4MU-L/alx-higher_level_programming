#!/usr/bin/node
// Displays a message depending of the number of arguments passed.

const args = process.argv.slice(2);

console.log(`${args[0]} is ${args[1]}`);
