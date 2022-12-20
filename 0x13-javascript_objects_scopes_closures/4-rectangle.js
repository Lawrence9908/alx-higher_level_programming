#!/usr/bin/node
class Rectange{
    constructor(w, h){
        if(w > 0 && h > 0){
            this.weight = w;
            this.height = h;
        }
    }
    print(){
        for(var row = 0; row <= this.weight; row++){
            for (var col = 0; col <=this.height; col++){
                console.log("x");
            }
        }
    }
    rotate(){
        this.weight = this.height;
        this.height = this.weight
    }
    double(){
        this.weight = this.weight * 2;
        this.height = this.height * 2;
    }
};