#!/usr/bin/node
let printed = 0;
exports.logMe = function (item) {
  console.log('%d: %s', printed, item);
  printed++;
};
