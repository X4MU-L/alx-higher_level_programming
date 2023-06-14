#!/usr/bin/node
// Displays the first argument if an integer.

const arg = process.argv.slice(2, 3).join();

if (Number.isNaN(Number(arg))) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(parseInt(arg)));
}
