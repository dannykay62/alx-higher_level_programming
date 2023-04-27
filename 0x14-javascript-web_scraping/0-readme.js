#!/usr/bin/node
const ss = require('fs');
ss.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
