"""
[easy]

在二叉树中，根节点位于深度 0 处，每个深度为 k 的节点的子节点位于深度 k+1 处。

如果二叉树的两个节点深度相同，但 父节点不同 ，则它们是一对堂兄弟节点。

我们给出了具有唯一值的二叉树的根节点 root ，以及树中两个不同节点的值 x 和 y 。

只有与值 x 和 y 对应的节点是堂兄弟节点时，才返回 true 。否则，返回 false。

 

示例 1：


输入：root = [1,2,3,4], x = 4, y = 3
输出：false
示例 2：


输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true
示例 3：



输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
 

提示：

二叉树的节点数介于 2 到 100 之间。
每个节点的值都是唯一的、范围为 1 到 100 的整数。

https://leetcode.cn/problems/cousins-in-binary-tree/description/?source=vscode
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        def f(node, x, y, depth):
            """返回x,y的父节点和深度"""
            if not node: return {}
            vals = []
            
            # 效率很低，很多重复判断
            if node.left:
                vals.append(node.left.val)
            if node.right:
                vals.append(node.right.val)
            
            ans = {}
            if x in vals:
                ans['x'] = (node, depth)
                # print("find x", ans['x'])
            if y in vals:
                ans['y'] = (node, depth)
                # print("find x")
            
            res1=f(node.left, x, y, depth+1)
            res2=f(node.right, x, y, depth+1)
            # print(res1, res2, ans)
            ans.update({**res1, **res2})
            return ans
            
        ans = f(root, x, y, 0)
        if 'x' not in ans or 'y' not in ans: return False
        # ❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️写代码要对每个语句负责❗️❗️❗️❗️❗️❗️❗️❗️❗️❗️
        # if 'x' or 'y' not in ans: return False
        return ans['x'][0].val!=ans['y'][0].val and ans['x'][1]==ans['y'][1]
