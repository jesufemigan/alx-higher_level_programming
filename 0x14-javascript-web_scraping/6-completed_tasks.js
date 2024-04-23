#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const obj = {};
  data.filter(todo => todo.completed === true)
    .map(todo => {
      if (obj[todo.userId] === undefined) {
        obj[todo.userId] = 1;
      } else {
        obj[todo.userId] += 1;
      }
      return null;
    });
  console.log(obj);
});
