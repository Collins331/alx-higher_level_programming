#!/usr/bin/node
const argument = process.argv.length - 2;

if (argument === 0) {
  console.log('No argument');
} else if (argument === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
