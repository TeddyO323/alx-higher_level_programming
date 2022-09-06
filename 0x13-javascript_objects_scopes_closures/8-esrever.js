#!/usr/bin/node
module.exports.esrever = function (list) {
  const listRev = [];
  const len = list.length;
  for (let i = 0; i < len; i++) {
    listRev.push(list.pop());
  }
  return listRev;
};
