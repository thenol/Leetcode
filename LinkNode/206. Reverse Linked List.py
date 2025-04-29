'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        Head=ListNode('')
        Head.next=None
        p=head
        while p:
            node=p
            p=p.next
            node.next=Head.next
            Head.next=node
        return Head.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        H = ListNode()
        q = head
        while q:
            p = H.next
            H.next = q
            q = q.next
            H.next.next = p
        
        return H.next
        