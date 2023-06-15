#!/usr/bin/node
// convert to different bases the number passed

exports.converter = function (base) {
  return (number) => {
    return (number.toString(base));
  };
};
