/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @return {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(strA, strB) {
    if (strA.toUpperCase() === strB.toUpperCase()) {
        return true;
    }
    else {
        return false;
    }
}

console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))

module.exports = { caseInsensitiveStringCompare };

// create a function to take in two arguements to compare
    // check if the two parameters are equal to each other
        // return true
    // else
        // false