#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  const dict = {};
  if (error) {
    console.log(dict);
  } else {
    const allTasks = JSON.parse(body);
    for (let i = 0; i < allTasks.length; i++) {
      if (allTasks[i].completed === true) {
        if (dict[allTasks[i].userId] === undefined) {
          dict[allTasks[i].userId] = 0;
        }
        dict[allTasks[i].userId] += 1;
      }
    }
    console.log(dict);
  }
});
