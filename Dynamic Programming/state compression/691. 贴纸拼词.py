"""
[hard]

我们有 n 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

您想要拼写出给定的字符串 target ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

返回你需要拼出 target 的最小贴纸数量。如果任务不可能，则返回 -1 。

注意：在所有的测试用例中，所有的单词都是从 1000 个最常见的美国英语单词中随机选择的，并且 target 被选择为两个随机单词的连接。

 

示例 1：

输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。
示例 2:

输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
 

提示:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target.length <= 15
stickers[i] 和 target 由小写英文单词组成

https://leetcode.cn/problems/stickers-to-spell-word/description/?source=vscode

"""

from collections import Counter
from math import inf
from functools import cache
class Solution:

    # 记忆化搜索 + 状态压缩；O(2^N×n×(c+N))
    """
    复杂度分析

    时间复杂度：O(2^m×n×(c+m))，其中 m 为 target 的长度，c 为每个 sticker 的平均字符数。一共有 O(2^m) 个状态。计算每个状态时，需要遍历 n 个 sticker。遍历每个 sticker 时，需要遍历它所有字符和 target 所有字符。

    空间复杂度：O(2^m)，记忆化时需要保存每个状态的贴纸数量。

    2^15*50*(10+15) = 40960000 约为 4 * 10^7

    """
    def minStickers(self, stickers: List[str], target: str) -> int:
        N = len(target)
        @cache
        def f(mask):
            """填充完成了target"""
            if mask == 0: return 0

            ans = inf
            for i, w in enumerate(stickers):
                cnt = Counter(w)
                tmp = mask
                for j in range(N):
                    if (tmp >> j) & 1 and target[j] in cnt and 0<cnt[target[j]]:
                        tmp = tmp ^ (1<<j)
                        cnt[target[j]] -= 1
                if tmp < mask: # 可能没有搜索到，剪枝；只有检索到之后才继续搜索
                    ans = min(ans, f(tmp)+1)
            
            return ans
        ans = f(2**N-1)
        return ans if ans < inf else -1


    # TLE； ❗️BFS或者DFS中的时候，千万记住状态复位的重要性
    # 另外，以后这种方式的算法就别尝试了，这里面穷举了所有可能的单词的组合，算法复杂度 O(N!)，一定会TLE
    def minStickers_1(self, stickers: List[str], target: str) -> int:
        N = len(target)
        @cache
        def f(mask, sel):
            """填充完成了target"""
            if mask == 0: 
                # print('found', sel)
                return len(sel)

            ans = inf
            for i, w in enumerate(stickers):
                cnt = Counter(w)
                tmp = mask
                choiced = False
                for j in range(N):
                    if (tmp >> j) & 1 and target[j] in cnt and 0<cnt[target[j]]:
                        choiced = True
                        tmp = tmp ^ (1<<j)
                        cnt[target[j]] -= 1
                if choiced: # 可能没有搜索到，剪枝；只有检索到之后才继续搜索
                    ans = min(ans, f(tmp, sel + (w,)))
            
            return ans
        ans = f(2**N-1, ())
        return ans if ans < inf else -1