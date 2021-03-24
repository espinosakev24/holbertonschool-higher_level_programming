#!/usr/bin/node
const d = require('./101-data.js').dict;
const dictKeys = {};

Array.from(new Set(Object.values(d))).forEach(i => dictKeys[i] = [] );
for(n in d) dictKeys[d[n]].push(n);
console.log(dictKeys);