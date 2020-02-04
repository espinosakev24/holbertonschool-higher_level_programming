#!/usr/bin/node
const number = process.argv[2];
if (isNaN(Number(number)) === false) {
  console.log(`My number: ${parseInt(number)}`);
} else {
  console.log('Not a number');
}
