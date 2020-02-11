#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!h || !w || h <= 0 || w <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
    this.print = function () {
      for (let n = 0; n < this.height; n++) {
        console.log('x'.repeat(this.width));
      }
    };
  }
};
