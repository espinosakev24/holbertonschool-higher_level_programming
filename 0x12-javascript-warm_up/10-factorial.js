#!/usr/bin/node
function factorial(a) { 
    if (isNaN(a) === true) {
        return 1;
    }   
    if (a === 0) { 
		return 1; 
	}
	return a * factorial(a - 1); 
}
a = parseInt(process.argv[2]);
console.log(factorial(a));