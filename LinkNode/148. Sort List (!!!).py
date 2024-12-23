'''
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(node):
            if not node.next:
                return node
            N=0
            p=node
            while p:
                p=p.next
                N+=1
            p=node
            count=1
            while count<N//2: # !!!!!!!
                p=p.next
                count+=1
            tail=p
            p=p.next
            tail.next=None
            left=merge(node)
            right=merge(p)
            res=mergeSort(left,right)
            return res
        def mergeSort(left,right):
            p=head=ListNode('')
            while left and right:
                if left.val<=right.val:
                    p.next=left
                    left=left.next
                else:
                    p.next=right
                    right=right.next
                p=p.next      
            if left:
                p.next=left
            if right:
                p.next=right
            return head.next
        if not head:
            return head
        return merge(head)