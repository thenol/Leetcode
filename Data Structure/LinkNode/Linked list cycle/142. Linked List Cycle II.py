'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

picture ......

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow-up:
Can you solve it without using extra space?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# version 1：

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        vis={}
        p=head
        while p and not id(p) in vis:
            vis[id(p)]=p
            p=p.next
        if p:
            return vis[id(p)]
        else:
            return None


# version 2：

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast=slow=head
        step_one=True
        while fast:
            if step_one:
                if fast.next and fast.next.next:
                    fast=fast.next.next
                    slow=slow.next
                else:
                    return None
                if fast==slow:
                    step_one=False
                    fast=head
            else:
                if fast==slow:
                    return fast
                fast=fast.next
                slow=slow.next
