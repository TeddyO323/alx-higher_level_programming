#!/usr/bin/node
/*
   The function Require includes modules
  that exist in separate file (4-rectangle)
  ========= Class Square ==================
  * Class square inherits from Class rectangle
*/
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
