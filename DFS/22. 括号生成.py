"""[medium]
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

 

示例 1：

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
示例 2：

输入：n = 1
输出：["()"]
 

提示：

1 <= n <= 8

https://leetcode.cn/problems/generate-parentheses/description/
"""

# 思路：数学归纳法，当知道 n-1 种情况之后，如何推理得到 n 的情况
## 在第 n 种情况下，最左边的括号一定是 ( , 那么剩下的 n-1 个括号可能在什么位置，
## 只能有两种情况，要么在 () 的内部，要么在 () 的右侧，注意不管是在内部还是在右侧，也必然是一个合法的括号字符串，因此只需要遍历可能性就行了
## 解释：只能在右侧的原因是，n 情况下的最左边是 (，所以肯定在右侧，不可能在左侧
## 因此：状态转移方程为 F(n+1) = ["(" + F(i) + ")" + F(n-i)] for i in range(0, n)，注意一共加起来，正好是 n+1 个括号对
## 即：第 n+1 时括号的种类 = "(" + {枚举可能性，括号内有0,1,2...,n个合法括号的时候情况} + ")" + {和前面对应n,n-1,...,0个合法括号的情况}
## https://leetcode.cn/problems/generate-parentheses/solutions/9251/zui-jian-dan-yi-dong-de-dong-tai-gui-hua-bu-lun-da/



## 方法一: 填表法
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        d = [[] for i in range(9)]
        d[0].append("")
        d[1].append("()")
        for i in range(2, n+1):
            for j in range(0, i):
                for k in range(0, len(d[j])):
                    for h in range(0, len(d[i-j-1])):
                        d[i].append("(" + d[j][k] + ")" + d[i-j-1][h])
        
        return d[n]

## 方法2: 记忆化搜索：
# 思路：
##  合法括号串的条件：左括号个数 大于等于 有括号；最终左右括号个数相同
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        m = n * 2  # 括号长度
        ans = []
        path = [''] * m  # 所有括号长度都是一样的 m
        # i=目前填了多少个括号
        # open=左括号个数，i-open=右括号个数
        def dfs(i: int, open: int) -> None:
            if i == m:  # 括号构造完毕
                ans.append(''.join(path))  # 加入答案
                return
            if open < n:  # 可以填左括号，
                path[i] = '('  # 直接覆盖
                dfs(i + 1, open + 1)  # 多了一个左括号
            if i - open < open:  # 可以填右括号，注意这个地方的分支，加完左括号后，如果满足条件，也可以添加右括号，因此才能遍历满足所有条件的可能性；都是从0开始计数的，或者其实本质应该是 i+1 - (open+1) < open，
                path[i] = ')'  # 直接覆盖
                dfs(i + 1, open)
        dfs(0, 0)
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/generate-parentheses/solutions/2071015/hui-su-bu-hui-xie-tao-lu-zai-ci-pythonja-wcdw/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。