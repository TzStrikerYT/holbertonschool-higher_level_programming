#!/usr/bin/node
const repeat = process.argv[2];
if (!isNaN(repeat)) {
  for (let i = 0; i < repeat; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
