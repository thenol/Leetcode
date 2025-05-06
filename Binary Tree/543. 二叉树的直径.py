"""
[easy]

给你一棵二叉树的根节点，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

 

示例 1：


输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。
示例 2：

输入：root = [1,2]
输出：1
 

提示：

树中节点数目在范围 [1, 104] 内
-100 <= Node.val <= 100

https://leetcode.cn/problems/diameter-of-binary-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 树形dp
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def depth(node):
            nonlocal ans
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            mx = max(left, right)+1
            ans = max(ans, left+right) # 记录最大直径
            return mx # 返回最大深度
        depth(root)
        return ans

    # 递归方法: ❌TLE
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 直径 = 左右子数最大深度之和
        if not root: return 0
        left = self.diameterOfBinaryTree(root.left)
        right = self.diameterOfBinaryTree(root.right)
        l = self.depth(root.left)
        r = self.depth(root.right)
        return max(left, right, l+r)
    
    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        return max(left, right) + 1
        