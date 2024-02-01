#!/usr/bin/node
const argv = process.argv;
const request = require('request');
const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
