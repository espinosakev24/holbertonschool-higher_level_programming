#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/';
request(url + process.argv[2], function (error, response, body) {
  if (error instanceof Error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
