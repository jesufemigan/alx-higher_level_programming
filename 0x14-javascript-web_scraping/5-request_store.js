#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  fs.writeFile(file, body, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
