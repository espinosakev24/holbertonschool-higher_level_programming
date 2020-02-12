#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error instanceof Error) {
    console.log(error);
  } else {
    const fs = require('fs');
    fs.writeFile(process.argv[3], body, function (err, contents) {
      if (err instanceof Error) {
        console.log(err);
      }
    });
  }
});
