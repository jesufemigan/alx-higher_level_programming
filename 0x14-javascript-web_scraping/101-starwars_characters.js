#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}/`;

request(url, async (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);

  try {
    for (const character of data.characters) {
      const characterData = await getDetails(character);
      console.log(characterData.name);
    }
  } catch (error) {
    console.log(error);
  }
});

function getDetails (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        reject(err);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}
