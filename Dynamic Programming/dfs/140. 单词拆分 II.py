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
# 思路：
"""
返回集合=>毫无疑问需要回溯

回溯判断依据 => 需要判断当前决策是否可行，也就需要判断 s[:i]是否可以表示在wordDict中，如果可以才能构成句子 => 构建d[i]判断依据 => 动态规划预处理

状态表示=>转移方程=>状态初始化 比较简单，直接见代码
"""


class Solution:
    # method 2: dfs
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # state: 
        word_set = set(wordDict)
        @cache
        def f(i):
            """返回s[:i]所有可能"""
            nonlocal word_set, s
            if i<=0: return []
            ans = []

            # ⭕️：这里是一个易错点，容易直接 return s[:i]，导致可能性判断的减少，记住这只是其中一种可能
            if s[:i] in word_set: 
                ans.append(s[:i])
            
            for j in range(11):
                t = s[i-j:i]
                res = None
                if t in word_set:
                    res = f(i-j)
                
                if res:
                    ans.extend([item + " " + t for item in res])
            return ans
        return f(len(s))

    # method 1
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # state: d[i] 表示 s[:i] 可以拆成 wordDict中单词
        # 0<=i<=len(s)
        d = [-1] * (len(s)+1)

        # initialization
        d[0] = 1

        # transition
        def f(i):
            """
            表示 s[:i] 可以拆成 wordDict中单词
            """
            if d[i] >= 0:
                return d[i]
            
            ans = False
            if s[:i] in wordDict:
                ans = 1
            else:
                for j in range(i):
                    if s[j:i] in wordDict and f(j):
                        ans = True
                        break
            d[i] = int(ans) 
            return d[i]
        
        for i in range(len(s)+1):
            f(i)
        # print(d)

        # 和 method 2一样，回溯法，但是结合了d[i]的判断
        def f1(i):
            """
            返回s[:i]的所有可能句子，注意不包括i
            i>=2
            """
            ### 易错点❌：
            # 这里直接return了，
            """
            if i == 0:
                return []
            elif s[0:i] in wordDict:
                return [s[0:i]] # 这只是其中一种可能啊，还有其他的
            """

            ans = []
            if i == 0:
                ans = []
            elif s[0:i] in wordDict:
                ans = [s[0:i]]

            for j in range(1,i):
                if s[j:i] in wordDict and d[j] == 1:
                    for ret in f1(j):
                        ans.append(f"{ret} {s[j:i]}")
            return ans
        
        return f1(len(s))