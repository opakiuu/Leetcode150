#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <sstream>
using namespace std;
//Stringstream 是用來字串分割的
// Given an input string s, reverse the order of the words.

// A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

// Return a string of the words in reverse order concatenated by a single space.

// Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

// Example 1:

// Input: s = "the sky is blue"
// Output: "blue is sky the"
// Example 2:

// Input: s = "  hello world  "
// Output: "world hello"
// Explanation: Your reversed string should not contain leading or trailing spaces.
// Example 3:

// Input: s = "a good   example"
// Output: "example good a"
// Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution
{
public:
    string reverseWords(string s)
    {
        stringstream ss(s);
        string word;
        vector<string> words;
        string result;
        // ss>>word 利用cin可以直接跳過所有空白，getline如果遇到連續delimiter會存入"" 空字串，所以要if(!word.empty()) 來判斷 
        while (getline(ss, word, ' '))
        {
            if(!word.empty()){
                words.push_back(word);
            }
            
        }
        for (int w = words.size() - 1; w >= 0; w--)
        {
            result += words[w];
            if (w > 0)
            {
                result += ' ';
            }
        }
        return result;
    }
};

int main(void)
{
    string s = "the sky is blue";
    Solution solution;
    cout << solution.reverseWords(s);
}
