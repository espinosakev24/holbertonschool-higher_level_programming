#!/usr/bin/node
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', function (err, contents) {
  if (err instanceof Error) {
    console.log(err);
  } else {
    console.log(contents);
  }
});
