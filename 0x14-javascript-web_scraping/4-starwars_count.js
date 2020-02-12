#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error instanceof Error) {
    console.log(error);
  } else {
    const all = JSON.parse(body).results;
    const allCharacters = [];
    let count = 0;
    let charReq = '';
    all.forEach(element => {
      allCharacters.push(element.characters);
    });
    for (let n = 0; n < allCharacters.length; n++) {
      for (let i = 0; i < allCharacters[n].length; i++) {
        charReq = allCharacters[n][i].split('/').slice(-2)[0];
        if (charReq === '18') {
          count++;
        }
      }
    }
    console.log(count);
  }
});
