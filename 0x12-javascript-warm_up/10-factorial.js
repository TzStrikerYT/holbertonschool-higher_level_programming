#!/usr/bin/node
function factorial (n) {
  if (n > 0) {
    const fact = n * factorial(n - 1);
    return fact;
  } else {
    return 1;
  }
}

const result = parseInt(process.argv[2]);
console.log(factorial(result));
