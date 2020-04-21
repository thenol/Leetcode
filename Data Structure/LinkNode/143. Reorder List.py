'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        N=0
        p=head
        while p:
            N+=1
            p=p.next
        floor=N//2
        p=head
        c=floor
        while c>=1: #
            p=p.next
            c-=1
        secHead=p
        p=secHead.next
        secHead.next=None
        while p:
            node=p
            p=p.next
            node.next=secHead.next
            secHead.next=node
        c=0
        p=head
        q=secHead.next
        secHead.next=None
        while q:
            if c%2==0:
                node=q
                q=q.next
                node.next=p.next
                p.next=node
            p=p.next
            c+=1
        return head
            


        
        