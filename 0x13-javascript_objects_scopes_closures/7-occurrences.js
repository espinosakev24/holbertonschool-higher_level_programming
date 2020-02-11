#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
    let count = 0;
    let idx  = 0;
    while(idx < list.length) {
        if(list[idx] == searchElement) {
            count++;
        }
        idx++;
    }
    return(count);
}