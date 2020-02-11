#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (!h || !w || h <= 0 || w <= 0) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let n = 0; n < this.height; n++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
};
