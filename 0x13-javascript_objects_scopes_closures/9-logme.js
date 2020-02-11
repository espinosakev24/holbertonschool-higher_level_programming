#!/usr/bin/node
var printed = 0;
exports.logMe = function (item) {
  printed++;
  console.log('%d %s', printed, item);
};
