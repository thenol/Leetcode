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

    # 思路：
    # https://leetcode.cn/problems/linked-list-cycle-ii/solutions/1999271/mei-xiang-ming-bai-yi-ge-shi-pin-jiang-t-nvsq/?envType=study-plan-v2&envId=top-100-liked
    """
    头节点到环入口需要走 a 步。设环长为 c。

    设相遇的时候，慢指针走了 b 步，那么快指针走了 2b 步。
    快指针比慢指针多走了 k 圈，即 2b−b=kc，得 b=kc。

    慢指针从环入口开始，在环中走了 b−a=kc−a 步到达相遇点。
    这说明从相遇点开始，再走 a 步，就恰好走到环入口了！
    虽然不知道 a 是多少，但如果让头节点和慢指针同时走，恰好 a 步后二者必定相遇，且相遇点就在环入口。
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head  # 初始化两个指针，slow（慢指针）和 fast（快指针），都指向链表的头节点
        while fast and fast.next:  # 当快指针不为空且快指针的下一个节点也不为空时，继续循环
            slow = slow.next      # 慢指针每次移动一步
            fast = fast.next.next  # 快指针每次移动两步
            if fast is slow:      # 如果快指针追上了慢指针，说明链表中存在环，且找到了相遇点
                while slow is not head:  # 从相遇点和头节点同时出发，每次一步，直到相遇
                    slow = slow.next
                    head = head.next
                return slow         # 两个指针相遇的节点就是环的入口节点
        return None                 # 如果循环结束且没有相遇，说明链表中没有环