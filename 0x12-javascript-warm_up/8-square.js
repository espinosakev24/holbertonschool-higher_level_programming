#!/usr/bin/node
const times = parseInt(process.argv[2]);
let n = 0;
while (n < times) {
    console.log("x".repeat(times));
    n++;
}