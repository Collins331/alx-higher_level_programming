#!/usr/bin/node
const firstAgrv = process.argv[2];

if (firstAgrv === undefined) {
  console.log('No argument');
} else {
  console.log(firstAgrv);
}
