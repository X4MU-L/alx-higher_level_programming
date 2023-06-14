#!/usr/bin/node
// Displays a message depending of the number of arguments passed.

const argLen = process.argv.slice(2).length;

if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
