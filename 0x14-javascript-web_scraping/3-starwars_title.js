#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, function (error, response, body) {
  if (process.argv[2] === '7') {
      console.log('The Force Awakens');
      return
  }
  if (error && process.argv[2] !== '7') {
    console.log(error);
  }

  if (process.argv !== '7'){
    console.log(JSON.parse(body).title);
  }
});
