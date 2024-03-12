#!/usr/bin/node

const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        let shape = '';
        for (let j = 0; j < this.width; j++) {
          shape += c;
        }
        console.log(shape);
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
