#!/usr/bin/node

const request = require('request');

const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const count = data.results.map(film => film.characters)
    .map(character => character.filter(film => film.includes('18')))
    .filter(arr => arr.length !== 0)
    .length;
  console.log(count);
});
