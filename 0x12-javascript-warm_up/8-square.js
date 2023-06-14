#!/usr/bin/node
// prints x times “C is fun" where x is from line args

const arg = process.argv.slice(2, 3).join();

if (!arg || Number.isNaN(Number(arg))) {
  console.log('Missing size');
} else {
  for (let i = Number(parseInt(arg)); i > 0; i--) {
    let x = '';
    for (let j = Number(parseInt(arg)); j > 0; j--) {
      x += 'X';
    }
    console.log(x);
  }
}
