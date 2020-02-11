const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
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
