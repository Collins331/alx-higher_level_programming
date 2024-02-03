#!/usr/bin/node
const argv = process.argv;
const request = require('request');

request.get(argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const data = JSON.parse(body);
  const results = data.results;
  const len = results.length;
  let count = 0;
  for (let i = 0; i < len; i++) {
    // console.log(results[i].characters);
    for (let j = 0; j < results[i].characters.length; j++) {
      if (results[i].characters[j] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
