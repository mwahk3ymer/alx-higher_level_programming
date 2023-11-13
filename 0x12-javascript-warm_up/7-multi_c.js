#!/usr/bin/node

function nPrint (n, txt) {
  if (Number.isNaN(n)) {
    console.log('Missing number of occurrences');
  } else if (n >= 0) {
    for (let i = 0; i < n; i++) {
      console.log(txt);
    }
  }
};

nPrint(Number.parseInt(process.argv[2]), 'C is fun');
