#!/usr/bin/node
const fs = require('fs');

const files = process.argv.slice(2);
const fileA = fs.readFileSync(files[0]);
const fileB = fs.readFileSync(files[1]);
fs.writeFileSync(files[2], fileA + fileB);
