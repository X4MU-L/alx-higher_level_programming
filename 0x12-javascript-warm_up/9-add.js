#!/usr/bin/node

// print add of two args to the command line

const arg = process.argv.slice(2);

function add (a, b) {
  console.log(a + b);
}

add(Number(parseInt(arg[0])), Number(parseInt(arg[1])));
