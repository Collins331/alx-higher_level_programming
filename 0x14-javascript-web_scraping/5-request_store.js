#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const argv = process.argv;

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(argv[3], body, 'utf-8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
