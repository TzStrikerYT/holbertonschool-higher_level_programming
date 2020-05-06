#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let arg = process.argv.sort();
  arg = arg.reverse()[1];
  console.log(parseInt(arg));
}
