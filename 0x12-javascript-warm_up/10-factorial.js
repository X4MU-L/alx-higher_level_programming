#!/usr/bin/node
// get the factorial of the command line argument

const arg = process.argv.slice(2, 3).join();

function factorial (num) {
  if (num === 1) {
    return (1);
  }
  return (num * factorial(num - 1));
}

if (Number.isNaN(Number(arg))) {
  console.log(1);
} else {
  console.log(factorial(Number(parseInt(arg))));
}
