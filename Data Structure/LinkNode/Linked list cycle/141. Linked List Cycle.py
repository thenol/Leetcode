'''
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# version 1:

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        vis={}
        p=head
        idx=0
        while p and not id(p) in vis:
            vis[id(p)]=idx
            p=p.next
            idx+=1
        if p:
            return True
        else:
            return False


# version 2:

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        fast = head
        slow = head
        while (fast):
            if fast.next and fast.next.next:
                fast = fast.next.next # fast exists, so the slow must exist
                slow = slow.next
            else:
                return False

            if fast == slow:
                return True
        return False
