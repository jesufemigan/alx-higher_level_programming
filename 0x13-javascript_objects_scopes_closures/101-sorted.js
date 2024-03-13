#!/usr/bin/node

const getDict = require('./101-data').dict;
const newDict = {};

for (const userId in getDict) {
  const times = getDict[userId];

  if (times in newDict) {
    newDict[times].push(userId);
  } else {
    newDict[times] = [userId];
  }
}
console.log(newDict);
