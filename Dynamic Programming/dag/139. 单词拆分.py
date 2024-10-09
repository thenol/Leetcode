'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dfs: 1.Pruning
        # find=False
        # rm=set()
        # def dfs(s,level):
        #     nonlocal find,rm
        #     if not s.strip():
        #         find=True
        #     else:
        #         for i in wordDict:
        #             if level==0:
        #                 rm=set()
        #             if not find:
        #                 if not i in rm:
        #                     idx=s.find(i)
        #                     if idx>=0:
        #                         print(i,'=>',s[:idx]+' '+s[idx+len(i):])
        #                         dfs(s[:idx]+' '+s[idx+len(i):],level+1)
        #                     else:
        #                         rm.add(i)
        # dfs(s,0)
        # return find
        
        # dp for Composition problem, prefix or suffix 
        wordDict=set(wordDict)
        
        d=[-1 for _ in range(len(s)+1)] # note the length is N+1, left-closed,right-open
        def dp(i):
            if not d[i]==-1:
                return d[i]
            if s[0:i] in wordDict: # s[0:i] can be composed of
                d[i]=True
                return d[i]
            ans=False
            for j in range(i):
                if s[j:i] in wordDict:
                    ans = ans or dp(j) # it returns if there exists one sub-problem optimal solution. However, 'dp(i) or ans' will find all sub-problem optimal solution and return 
            d[i]=ans
            return d[i]
        return dp(len(s))

# 方法2——回溯:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
            @lru_cache
            def f(s):
                ans = False
                if s in wordDict:
                    return True
                for w in wordDict:
                    if s.startswith(w):
                        ans = ans or f(s[len(w):])
                
                return ans
            
            return f(s)