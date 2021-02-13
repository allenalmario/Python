/* 
Given an arr and a separator string, output a string of every item in the array separated by the separator.

No trailing separator at the end
Default the separator to a comma with a space after it if no separator is provided
*/

const arr1 = [1, 2, 3];
const separator1 = ", ";
const expected1 = "1, 2, 3";

const arr2 = [1, 2, 3];
const separator2 = "-";
const expected2 = "1-2-3";

const arr3 = [1, 2, 3];
const separator3 = " - ";
const expected3 = "1 - 2 - 3";

const arr4 = [1];
const separator4 = ", ";
const expected4 = "1";

const arr5 = [];
const separator5 = ", ";
const expected5 = "";

/**
 * Converts the given array into a string of items separated by the given separator.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<string|number|boolean>} arr The items to be joined as a string.
 * @param {string} separator To separate each item of the given arr.
 * @return {string} The given array items as a string separated by the given separator.
 */
function join(arr, separator) {
    randString = ""
    if (arr.length < 2) {
        for (var i = 0; i < arr.length; i++) {
            randString += arr[i];
        }
    }
    else {
        for (var i = 0; i < arr.length; i++) {
            if (i == arr.length - 1) {
                randString += arr[i];
            }
            else {
                randString += (arr[i] + separator); 
            }
        }
    }
    return randString;
}

console.log(join([1,2,3], ", "))
console.log(join([1,2,3], "-"))
console.log(join([1,2,3], " - "))
console.log(join([1],", "))
console.log(join([], ", "))

module.exports = { join };

// create function to take in two parameters
    // variable to carry string
    // if length < 2
        // for loop to go through that loop
        // take value of i and make it equal to variable
    // else
        // for loop to go through array length more than 1
            // if i equals last value
                // add that to string without seperator
            // else
                // add that value to string with seperator
    // return the string to function call


/*****************************************************************************/

/* 
Book Index
Given an arry of ints representing page numbers
return a string with the page numbers formatted as page ranges when the nums span a consecutive range
*/

const nums1 = [1, 13, 14, 15, 37, 38, 70];
const expected1 = "1, 13-15, 37-38, 70";

/**
 * Turns the given arr of page numbers into a string of comma hyphenated
 * page ranges.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums Page numbers.
 * @return {string} The given page numbers as comma separated hyphenated
 *    page ranges.
 */
function bookIndex(nums) {}

module.exports = { bookIndex };