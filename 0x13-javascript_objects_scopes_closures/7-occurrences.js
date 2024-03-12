#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const newList = list.filter(a => a === searchElement);
  return newList.length;
};
