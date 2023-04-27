#!/usr/bin/node
const req = require('request');
let url = 'https://swapi.co/api/films/' + process.argv[2];
req(url, function (error, response, body) {
  console.log(error || JSON.parse(body).title);
});
