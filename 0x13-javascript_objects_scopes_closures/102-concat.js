#!/usr/bin/node

const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const file1 = fs.readFileSync(fileA);
const file2 = fs.readFileSync(fileB);
fs.writeFileSync(fileC, file1 + file2);
