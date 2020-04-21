'''
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# The appliance of reverse order node
# Note: the way that the parameter passed into the function
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node_list=[]
        cur_list=[]
        pre=''          #！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！important
        def inorder(node):
            nonlocal pre
            if node:
                inorder(node.left)
                if not pre=='' and node.val<pre.val:
                    if not node_list:
                        node_list.append(pre)# remember the first reverse order node
                        cur_list.append(node)
                    else:
                        node_list.append(node) # remember the second reverse order node if there is 
                pre=node
                inorder(node.right)
        inorder(root)
        if len(node_list)==2:
            node_list[0].val,node_list[1].val=node_list[1].val,node_list[0].val
        else:
            node_list[0].val,cur_list[0].val=cur_list[0].val,node_list[0].val
        return root