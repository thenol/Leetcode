"""
[medium]

给你一个正整数数组 arr，考虑所有满足以下条件的二叉树：

每个节点都有 0 个或是 2 个子节点。
数组 arr 中的值与树的中序遍历中每个叶节点的值一一对应。
每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

如果一个节点有 0 个子节点，那么该节点为叶节点。

 

示例 1：


输入：arr = [6,2,4]
输出：32
解释：有两种可能的树，第一种的非叶节点的总和为 36 ，第二种非叶节点的总和为 32 。 
示例 2：


输入：arr = [4,11]
输出：44
 

提示：

2 <= arr.length <= 40
1 <= arr[i] <= 15
答案保证是一个 32 位带符号整数，即小于 231 。

https://leetcode.cn/problems/minimum-cost-tree-from-leaf-values/description/?source=vscode
"""

# 核心思路：与 《1000. 合并石头的最低成本.py》 完全相同，只是k=2

from functools import cache
from math import inf
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # state: d[i][j] 表示arr[i:j]合并成的最小可能总和
        # 0<=i<N; 0<=j<=N
        N = len(arr)

        @cache
        def f(i, j): # i, j, p=1
            """表示arr[i:j]合并成的最小可能总和"""
            nonlocal arr
            # initialization
            if j-i==2: return arr[i]*arr[i+1]
            if j-i==1: return 0 # 叶子节点

            # transition
            ans = inf
            for k in range(i+1, j):
                ans = min(ans, f(i,k)+f(k,j)+max(arr[i:k])*max(arr[k:j]))
            
            return ans
        return f(0, N)
        