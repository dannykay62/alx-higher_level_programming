#!/usr/bin/node
const ss = require('fs');
ss.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
