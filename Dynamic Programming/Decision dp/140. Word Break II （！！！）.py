'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dic=set(wordDict)
        ans=[]
        # optimize the algorithm by dynamic programming
        d=[-1 for _ in range(len(s))]+[True]
        def dp(i): # focus on prefix
            if d[i]!=-1:
                return d[i]
            if s[i:] in dic:
                d[i]=True
            else:
                ans=False
                for j in range(i+1,len(s)+1):
                    if s[i:j] in dic:
                        ans=dp(j) or ans # the most important step
                d[i]=ans
            return d[i]
        
        def dfs(s,path,p):
            if p==len(s):
                ans.append(' '.join(path))
            else:
                for i in range(p+1,len(s)+1):  # once again, note the left-closed right-open "[)"
                    if s[p:i] in dic and d[i]==True:
                        # print(p,i,s[p:i])
                        dfs(s,path[:]+[s[p:i]],i)
        dp(0)
        print(d)
        dfs(s,[],0)
        return ans