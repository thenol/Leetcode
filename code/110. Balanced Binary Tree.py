'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/balanced-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def preorder(node,depth):
            nonlocal mxdepth
            if node:
                preorder(node.left,depth+1)
                mxdepth=mxdepth if mxdepth>depth+1 else depth+1
                preorder(node.right,depth+1)
        mxdepth=0
        preorder(root.left,0)
        l_depth=mxdepth
        mxdepth=0
        preorder(root.right,0)
        r_depth=mxdepth
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(l_depth-r_depth)<=1:
            return True
        else:
            return False
        
