'''
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        HEAD=ListNode(head.val-1)
        HEAD.next=head
        t,p=HEAD,head
        last=t.val
        count=0
        
        while p:
            if not p.val==last:
                if count==1: # unique
                    t=t.next
                    t.val=last
                last=p.val
                p=p.next
                count=1 
            else:
                count+=1
                p=p.next
        
        if count==1:
            t=t.next
            t.val=last
        if t.next==head:
            return None
        else:
            t.next=None
        return head