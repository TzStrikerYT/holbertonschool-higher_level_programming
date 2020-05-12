#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const fs = require('fs');
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    fs.writeFileSync(process.argv[3], error, 'utf8');
  } else {
    fs.writeFileSync(process.argv[3], body, 'utf8');
  }
});
