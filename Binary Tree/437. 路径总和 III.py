"""
[medium]

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

示例 1：



输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。
示例 2：

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3
 

提示:

二叉树的节点个数的范围是 [0,1000]
-109 <= Node.val <= 109 
-1000 <= targetSum <= 1000 

https://leetcode.cn/problems/path-sum-iii/description/?envType=study-plan-v2&envId=top-100-liked
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        cnt = Counter()
        cnt[0] = 1
        def dfs(node, pre_s):
            nonlocal ans, targetSum
            if not node: return 
            
            pre_s = pre_s+node.val
            ans += cnt[pre_s-targetSum] # 注意先算当前前缀和的情况，否则容易造成误判，多算；例：root = [1]，target = 0，预期0，输出1

            cnt[pre_s] += 1
            dfs(node.left, pre_s)
            dfs(node.right, pre_s)
            cnt[pre_s] -= 1

        dfs(root, 0)
        return ans


    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        def dfs(node, pre_s):
            nonlocal ans, targetSum
            if not node: return 
            
            pre_s = pre_s+node.val
            cnt[pre_s] += 1 # 
            ans += cnt[pre_s-targetSum]

            if node.left: # 因为前面判断了 node 是 None的情况，因此可以省略
                dfs(node.left, pre_s)
            if node.right:
                dfs(node.right, pre_s)

            cnt[pre_s] -= 1
        dfs(root, 0)
        return ans
