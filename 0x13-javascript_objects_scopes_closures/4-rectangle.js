#!/usr/bin/node
class Rectange{
    constructor(w, h){
        if(w > 0 && h > 0){
            this.width = w;
            this.height = h;
        }
    }
    print(){
        for(let col = 0; col <= this.height; col++){
            for (let row = 0; row <=this.width; row++){
                console.log("x");
            }
        }
    }
    rotate(){
        this.width = this.height;
        this.height = this.width;
    }
    double(){
        this.width = this.width * 2;
        this.height = this.height * 2;
    }
};
module.exports = Rectange;