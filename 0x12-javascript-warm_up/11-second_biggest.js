#!/usr/bin/node
const arr = process.argv.slice(2).map(x => parseInt(x));
if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  const max = Math.max(...arr);
  arr.splice(arr.indexOf(max), 1);
  if (arr.length === 0) {
    console.log(max);
  } else {
    console.log(Math.max(...arr));
  }
}
