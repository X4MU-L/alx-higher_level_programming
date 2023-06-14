#!/usr/bin/node
// Displays a message depending of the number of arguments passed.

const args = process.argv.slice(2).join();

if (!args) {
  console.log('No argument');
} else {
  console.log(args.split(',')[0]);
}
