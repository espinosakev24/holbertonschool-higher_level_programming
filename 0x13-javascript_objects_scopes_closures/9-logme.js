#!/usr/bin/node
var printed = 0;
exports.logMe = function (item) {
  console.log('%d: %s', printed, item);
  printed++;
};
