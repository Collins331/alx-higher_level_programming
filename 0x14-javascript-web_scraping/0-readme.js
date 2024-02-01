#!/usr/bin/node
const argv = process.argv;
const fs = require('fs');
fs.readFile(argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});
