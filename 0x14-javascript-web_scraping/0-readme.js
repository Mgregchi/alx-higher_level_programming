#!/usr/bin/node

const fs = require('fs');

const filePath = process.argv[2];

try {
  const content = fs.readFileSync(filePath, 'utf-8');
  console.log(content);
} catch (error) {
  console.error(error);
}
