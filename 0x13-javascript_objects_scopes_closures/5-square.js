#!/usr/bin/node
const Rectangle = require('./5-ractangle');
class Square extends Rectangle{
    constructor(size){
        super(size, size);
    }
};
module.exports = Square;
