#!/usr/bin/node
let arr = process.argv.slice(2).map(Number);
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  const max = Math.max(arr);
  arr.splice(arr.indexOf(max));
  if (arr.length === 0) {
    console.log(max);
  } else {
    console.log(Math.max.apply(Math, arr));
  }
}
