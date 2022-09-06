#!/usr/bin/node
module.exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      counter++;
    }
  }
  return counter;
};
