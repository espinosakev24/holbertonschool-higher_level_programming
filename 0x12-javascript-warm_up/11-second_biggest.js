#!/usr/bin/node
let arr = process.argv.slice(2);
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  arr = arr.map(function (x) {
    return Number(x);
  });
  const max = Math.max.apply(Math, arr);
  arr.splice(arr.indexOf(max));
  if (arr.length === 0) {
    console.log(undefined);
  } else {
    console.log(Math.max.apply(Math, arr));
  }
}
