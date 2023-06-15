#!/usr/bin/node
// create a square class object that inherits from Rectangle

const Square1 = require('./5-square');
module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    for (let i = this.height; i > 0; i--) {
      console.log(c.repeat(this.width));
    }
  }
};
