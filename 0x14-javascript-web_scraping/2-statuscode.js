#!/usr/bin/node
const request = require('request');
const argv = process.argv;

request.get(argv[2], (error, response) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(`code: ${response.statusCode}`);
});
