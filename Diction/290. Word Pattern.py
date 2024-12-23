'''
[easy]

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def wordPattern(self, pattern: str, strs: str) -> bool:
        words=strs.split(' ')
        if len(pattern)!=len(words):
            return False
        dic={}
        dic1={}
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                dic[pattern[i]]=words[i]
            else:
                if dic[pattern[i]]!=words[i]:
                    return False
            if words[i] not in dic1:
                dic1[words[i]]=pattern[i]
            else:
                if dic1[words[i]]!=pattern[i]:
                    return False
        return True