#!/usr/bin/node
exports.esrever = function (list) {
    let newList = [];
    let listLen = list.length;
    while(listLen - 1 >= 0) {
        listLen = listLen - 1;
        newList.push(list[listLen]);
    }
    return newList
}