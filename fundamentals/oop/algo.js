// const arr1 = [1, 2, 3]; // array
// const separator1 = ", "; // string
// const expected1 = "1, 2, 3"; // output should be a string

// const arr2 = [1, 2, 3];
// const separator2 = "-";
// const expected2 = "1-2-3";

// const arr3 = [1, 2, 3];
// const separator3 = " - ";
// const expected3 = "1 - 2 - 3";

// const arr4 = [1];
// const separator4 = ", ";
// const expected4 = "1";

// const arr5 = [];
// const separator5 = ", ";
// const expected5 = "";



// function separation(arr, type) {

//     var holder = ''

//     for (i = 0; i < arr.length; i++){

//         holder += arr[i]
//         if (i !== arr.length - 1){
//             holder += type
//         }

//     }

//     return holder

// }

// console.log(separation(arr1, separator1))





// take in string(s)
// var longest palindrom
// test palindrom
// for loop starting from 0 to string length
//      for loop stating from 0 decrementing from end
// add to arr of test palindrom
// if number == number && test > longest longest = test palindrom
// 

/* 
  String: Is Palindrome
  Create a function that returns a boolean whether the string is a strict palindrome. 
    - palindrome = string that is same forwards and backwards
  
//   Do not ignore spaces, punctuation and capitalization
//  */

// const str1 = "a x a";
// const expected1 = true;

// const str2 = "racecar";
// const expected2 = true;

// const str3 = "Dud";
// const expected3 = false;

// const str4 = "oho!";
// const expected4 = false;


// /**
//  * Determines if the given str is a palindrome (same forwards and backwards).
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {boolean} Whether the given str is a palindrome or not.
//  */
// function isPalindrome(str) { }

// module.exports = { isPalindrome };

/*****************************************************************************/

/* 
  Longest Palindrome
  For this challenge, we will look not only at the entire string provided, but also at the substrings within it. Return the longest palindromic substring. 
  Strings longer or shorter than complete words are OK.
  All the substrings of "abc" are:
  a, ab, abc, b, bc, c
*/

// const { isPalindrome } = require("./isPalindrome");
const str1 = "what up, daddy-o?";
const expected1 = "dad";

const str2 = "uh, not much";
const expected2 = "u";

const str3 = "Yikes! my favorite racecar erupted!";
const expected3 = "e racecar e";

const str4 = "a1001x20002y5677765z";
const expected4 = "5677765";

const str5 = "a1001x20002y567765z";
const expected5 = "567765";

// /**
//  * Finds the longest palindromic substring in the given string.
//  * - Time: O(?).
//  * - Space: O(?).
//  * @param {string} str
//  * @returns {string} The longest palindromic substring from the given string.
//  */
// function longestPalindromicSubstring(str) { }

// module.exports = { longestPalindromicSubstring: longestPal };

/*****************************************************************************/




// take in string(s)
// var longest palindrom
// test palindrom
// for loop starting from 0 to string length
//      for loop stating from 0 decrementing from end
// add to arr of test palindrom
// if number == number && test > longest longest = test palindrom
// 



// for (i)// take in string(s)
    // var longest palindrom
    // test palindrom
    // for loop starting from 0 to string length
    //      for loop stating from 0 decrementing from end
    // add to arr of test palindrom
    // if number == number && test > longest longest = test palindrom
    // 

function Paltester(arr) {

        var testPalindrome = ''
        var longestPalindrome = ''

        for (var i = 0; i < arr.length; i++) {

            for (var x = arr.length; x > 0; x--) {

                if (arr[x] == arr[i]) {
                    testPalindrome += arr[x]
                }
                if (testPalindrome > longestPalindrome) {
                    longestPalindrome = testPalindrome
                }

            }

        }
    return longestPalindrome
}


console.log(Paltester(str1))