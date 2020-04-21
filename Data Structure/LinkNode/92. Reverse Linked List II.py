'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # so easy
        HEAD=ListNode(-1)
        HEAD.next=head
        tail=HEAD
        count=n-m
        p=head
        i=1
        while i<m:
            tail=tail.next
            p=p.next
            i+=1
        while count>=1:
            tmp=tail.next
            tail.next=p.next
            p.next=p.next.next
            tail.next.next=tmp
            count-=1
        return HEAD.next
        