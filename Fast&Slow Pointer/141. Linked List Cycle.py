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


"""
思路：


https://leetcode.cn/problems/linked-list-cycle/solutions/1999269/mei-xiang-ming-bai-yi-ge-shi-pin-jiang-t-c4sw/?envType=study-plan-v2&envId=top-100-liked
"""

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
"""
思路：
想象在一个环形的跑道上，一个跑得快的人和一个跑得慢的人同时出发。如果跑道是环形的，跑得快的人最终一定会再次追上跑得慢的人。在链表中，如果存在环，快指针和慢指针也会遵循这个规律最终相遇。如果不存在环，快指针会先到达链表的末尾
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head  # 初始化两个指针，slow（慢指针）和 fast（快指针），都指向链表的头节点
        while fast and fast.next:  # 当快指针不为空且快指针的下一个节点也不为空时，继续循环
            slow = slow.next      # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步
            if fast is slow:      # 如果快指针追上了慢指针，说明链表中存在环
                return True
        return False             # 如果循环结束，说明快指针到达了链表末尾（没有环）