#!/usr/bin/node
/**
 * function to count number of occurrences in a list
 * @param {list} list - list ti examine
 * @param {number} searchElement - element to search for
 * @returns {number} - the number of occurrences in a list
 */
exports.nbOccurences = function (list, searchElement) {
  let index, count = 0;
  for (index = 0; index < list.length; index++){
     if(list[index] == searchElement){
        count = count + 1;
     }  
  }
  return count;
}