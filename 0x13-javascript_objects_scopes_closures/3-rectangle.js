#!/usr/bin/node
class Rectange{
    constructor(w, h){
        if(w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }
    print(){
        for(let row = 0; row <= this.height; row++){
            for (let col = 0; col <=this.width; col++){
                console.log("X");
            }
        }
    }
};
module.exports = Rectange;