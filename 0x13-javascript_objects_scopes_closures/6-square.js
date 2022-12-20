#!/usr/bin/node

class Square extends Rectangle{
    charPrint(c){
        if (c == undefined){
            this.charPrint()
        }
    }
}