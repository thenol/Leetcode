'''
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def tail(node):
            while node.right:
                node=node.right
            return node
        def postorder(node):
            if not node:
                return None
            if node and not node.left and not node.right: # return when it is leaf
                return node
            lhead=postorder(node.left)
            rhead=postorder(node.right)
            if lhead:
                last=tail(lhead)
                last.right=rhead
                node.right=lhead
                node.left=None
            return node
        postorder(root)
                