#!/usr/bin/node
const Rectangle = require("./4-rectangle")
class Square extends Rectangle{
    charPrint(c){
        if (c != undefined){
            for (let col = 0; col <= this.height; col++){
                for (let row = 0; row <= this.width; row++){
                    console.log("X");
                }
            }
        }else{
            this.print();
        }
    }
};
module.exports = Square;