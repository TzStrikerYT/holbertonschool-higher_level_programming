#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const antilles = '/18/';

request(url, function (error, response, body) {
  const movie = JSON.parse(body).results;
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    for (let i = 0; i < movie.length; i++) {
      const characters = movie[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes(antilles)) { count += 1; }
      }
    }
    console.log(count);
  }
});
