#!/usr/bin/node
const repeat = process.argv[2];
if (!isNaN(repeat)) {
  for (let i = 0; i < repeat; i++) {
    for (let j = 0; j < repeat; j++) {
      process.stdout.write('X');
    }
    process.stdout.write('\n');
  }
} else {
  console.log('Missing size');
}
