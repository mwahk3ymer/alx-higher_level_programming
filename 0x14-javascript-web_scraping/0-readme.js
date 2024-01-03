#!/usr/bin/node
/**
 * Reads and prints the content of a file.
 */

const fs = require('fs');

function readAndPrintFile(filePath) {
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    console.error(`An error occurred: ${error.message}`);
  }
}

if (process.argv.length !== 3) {
  console.log('Usage: ./script.js <file_path>');
  process.exit(1);
}

const filePath = process.argv[2];
readAndPrintFile(filePath);
