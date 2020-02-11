#!/usr/bin/node
const Squarep = require('./5-square');
module.exports = class Square extends Squarep {
  constructor (size) {
    super(size, size);
  }

  charPrint (C) {
    if (!C) {
      for (let n = 0; n < this.width; n++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (let n = 0; n < this.width; n++) {
        console.log(C.repeat(this.width));
      }
    }
  }
};
