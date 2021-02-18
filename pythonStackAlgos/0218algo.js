/* 
Given a string,
return a new string with the duplicates excluded
Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "banana";
const expected3 = "ban";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @return {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    newDict = {}
    for (i = 0; i < str.length; i++) {
        newDict[str[i]] = ""
    }
    newStr = ""
    for (key in newDict) {
        if (newDict.hasOwnProperty(key)) {
            newStr += key
        }
    }
    return newStr
}

console.log(stringDedupe(str1))
console.log(stringDedupe(str2))
console.log(stringDedupe(str3))

module.exports = { stringDedupe };