'''
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return 
        else:
            le=0
            p=head
            while p:
                p=p.next
                le+=1
            mid=le//2
            le,p=0,head
            while p and le<mid-1:
                p=p.next
                le+=1
            if mid>=1:
                r_head=p.next.next
                root=TreeNode(p.next.val)
                p.next=None
                root.left=self.sortedListToBST(head)
                root.right=self.sortedListToBST(r_head)
            else:
                root=TreeNode(p.val)
            return root
            