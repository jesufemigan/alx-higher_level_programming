#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);

  data.characters.map(character => {
    request(character, (err, res, body) => {
      if (err) {
        console.log(err);
      }
      const newData = JSON.parse(body);
      console.log(newData.name);
    });
    return null;
  });
});
