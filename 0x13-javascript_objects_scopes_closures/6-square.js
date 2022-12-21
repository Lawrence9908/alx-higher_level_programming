#!/usr/bin/node
class Square extends Rectangle{
    charPrint(c){
        if (c == undefined){
            this.print();
        }
    }
};
module.exports = Square;