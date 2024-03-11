#!/usr/bin/node

let firstArg = process.argv[2];
if (isNaN(firstArg)) {
  console.log('Missing number of occurences');
} else {
  while (firstArg > 0) {
    console.log('C is fun');
    firstArg--;
  }
}
