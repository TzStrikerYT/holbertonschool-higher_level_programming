#!/usr/bin/node
if (process.argv[2] && process.argv[3]) {
  const array = process.argv.slice(2, process.argv.length);
  const maxn = Math.max.apply(null, array);
  const max = maxn.toString(10);
  const maxi = array.indexOf(max);
  array[maxi] = -Infinity;
  const secondMax = Math.max.apply(null, array);
  array[maxi] = max;
  console.log(secondMax);
} else {
  console.log('0');
}
