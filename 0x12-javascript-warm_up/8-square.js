#!/usr/bin/node
const times = parseInt(process.argv[2]);
if (isNaN(times)) {
  console.log('Missing size');
}
let n = 0;
while (n < times) {
  console.log('x'.repeat(times));
  n++;
}
