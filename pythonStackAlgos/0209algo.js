/* 

Possible topics to explore: 
1.) Iterating over strings
2.) Immutability
3.) while loops / or for loops ?
4.) (extra) let, const and var

*/

/*
String: Reverse
Given a string,
return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @return {string} The given str reversed.
 */
function reverseString(str) {
    var reverse_string = ""
    for (var i = 0; i < str.length; i++) // can start from the last index of the str and go backwards
        reverse_string = reverse_string + str[(str.length - 1) - i] // reverse_string += str[i]
    return reverse_string
}

console.log(reverseString(str1), reverseString(str1) == expected1);
console.log(reverseString(str2), reverseString(str2) == expected2);

module.exports = { caseInsensitiveStringCompare };

/*************************************************************/

// create function that takes in a string
    // create a variable to hold and empty string to add on
    // start a for loop to go through the string
        // take the variable, add it to the current value at i and equal it to variable
    // return the string, should be reversed