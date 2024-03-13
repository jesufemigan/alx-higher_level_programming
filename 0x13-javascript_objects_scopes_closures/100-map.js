#!/usr/bin/node

const list = require('./100-data').list;

const newList = list.map((index, value) => value * index);

console.log(list);
console.log(newList);
