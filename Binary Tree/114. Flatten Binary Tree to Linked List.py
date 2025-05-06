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
    # O(n); O(1)
    def flatten(self, root: TreeNode) -> None:
        """
        将二叉树就地扁平化为一个单链表。
        
        思路：
            这段代码实现了将二叉树扁平化为单链表的功能，其核心思想是对于每一个存在左子树的节点，找到其左子树的最右侧节点，然后将当前节点的右子树连接到该最右侧节点的右边，接着将当前节点的左子树置为空，最后将当前节点的右子树指向原来的左子树。这样就将左子树“移动”到了右子树的位置。这个过程不断重复，直到遍历完整个树。

        Args:
            root: 二叉树的根节点。扁平化后，root 将会是单链表的头节点。
        """
        curr = root  # 初始化当前节点为根节点；链接好左子树的首尾两个节点
        while curr:  # 遍历整个树
            if curr.left:  # 如果当前节点存在左子树
                # 找到左子树的最右侧节点（前驱节点）
                predecessor = nxt = curr.left
                while predecessor.right:
                    predecessor = predecessor.right

                # 将当前节点的右子树连接到前驱节点的右子树；
                predecessor.right = curr.right

                # 将当前节点的左子树置为空
                curr.left = None

                # 将当前节点的右子树指向原来的左子树，完成连接
                curr.right = nxt
            # 如果当前节点没有左子树，则直接移动到右子节点
            curr = curr.right
                

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
    