#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const size = list.length - 1;
  for (let i = size; i >= 0; i--) {
    newList.push(list[i]);
  }
  return newList;
};
