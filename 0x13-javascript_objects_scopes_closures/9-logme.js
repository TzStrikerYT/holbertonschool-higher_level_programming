#!/usr/bin/node
exports.logMe = function (item) {
  if (this.flag === undefined) {
    this.flag = 0;
  }
  console.log(this.flag + ':', item);
  this.flag++;
};
