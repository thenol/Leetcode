"""
[medium]

正整数 n 代表生成括号的对数，请设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8
 

注意：本题与主站 22 题相同： https://leetcode-cn.com/problems/generate-parentheses/

https://leetcode.cn/problems/IDBivT/description/?source=vscode
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2
        ans = []
        path = [''] * m
        def dfs(i: int, open: int) -> None:
            """
            当前填写了i个数，且填写了open个 "(" 对应的种类
            """
            if i == m:
                ans.append(''.join(path))
                return
            if open < n:  # 左括号小于左括号总量，可以填左括号
                path[i] = '('
                dfs(i + 1, open + 1)
            if i - open < open:  # 左边大于右边，可以填右括号
                path[i] = ')'
                dfs(i + 1, open)
        dfs(0, 0) 
        return ans
