#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <sstream>
using namespace std;

// Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

// You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

// Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

// For the last line of text, it should be left-justified, and no extra space is inserted between words.

// Note:

// A word is defined as a character sequence consisting of non-space characters only.
// Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
// The input array words contains at least one word.

// Example 1:

// Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
// Output:
// [
//    "This    is    an",
//    "example  of text",
//    "justification.  "
// ]
// Example 2:

// Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
// Output:
// [
//   "What   must   be",
//   "acknowledgment  ",
//   "shall be        "
// ]
// Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
// Note that the second line is also left-justified because it contains only one word.
// Example 3:

// Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
// Output:
// [
//   "Science  is  what we",
//   "understand      well",
//   "enough to explain to",
//   "a  computer.  Art is",
//   "everything  else  we",
//   "do                  "
// ]

class Solution
{
public:
    vector<string> fullJustify(vector<string> &words, int maxWidth)
    {
        
        return {"This    is    an",
                "example  of text",
                "justification.  "};
    }
};

int main(void)
{
    vector<string> words = {"This", "is", "an", "example", "of", "text", "justification."};
    int maxWidth = 16;
    Solution solution;
    for (auto f : solution.fullJustify(words, maxWidth))
    {
        cout << f;
        cout<<endl;
    }
}

// wl + Space + w2 + space ... + space .-
// mex Width

// Otheraise :
// GAP           //Gap
// totol Chos: Wordl + space + word2 + space + word 3
//                4      1       2        1      2
// (maxWidth - total Chors ) / gaps
// SPACES (17 - 10 ) / 2 = 3
// rest : (17-10) % 2 = | the first gap has 3+1 spaces
// Some gaps may have 1) more space than others
// at most