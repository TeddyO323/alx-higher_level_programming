#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      // to initialize instance you need write this
      this.width = w;
      this.height = h;
    }
  }

  /*
      Method print that prints the rectangle using the character X
    */
  print () {
    const character = 'X';
    for (let i = 0; i < this.height; i++) {
      console.log(character.repeat(this.width));
    }
  }

  /*
      Method rotate that exchanges
      the width and the height of the rectangle
    */
  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  /*
      method Double that multiples the width and the height
      of the rectangle by 2
    */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
