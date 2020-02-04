#!/usr/bin/node
let idx = 0;
const x = parseInt(process.argv[2]);
if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
} else {
  if (x > 0) {
    while (idx !== x) {
      idx = idx + 1;
      console.log('C is fun');
    }
  }
}
