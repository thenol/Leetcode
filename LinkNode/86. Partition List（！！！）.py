'''
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # chain operation
        # think thoroughly before you take actions
        # Coding as easy as possible
        
        HEAD=ListNode(-1)
        def swap_success(p,q):
            qnext=q.next
            q.next=qnext.next
            qnext.next=p.next
            p.next=qnext
        HEAD.next=head
        p=HEAD
        while p.next and p.next.val<x:p=p.next
        q=p.next
        asc=True
        while q and q.next:
            if q.next.val<x:
                print(q.val,q.next.val)
                swap_success(p,q)
                p=p.next
                asc=False
            else:
                q=q.next
            # print(HEAD)
        if asc:
            return HEAD.next
        return HEAD.next
        