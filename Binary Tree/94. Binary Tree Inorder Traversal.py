'''
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack=[]
        ans=[]
        cur=root # 用一个指针
        while True:
            if cur: # 当cur为空时弹出下一个元素
                stack.append(cur)
                cur=cur.left
            else:
                if stack:
                    x=stack.pop()
                    ans.append(x.val)
                    cur=x.right # cur 可以指向空，但是不会重复；也就是当没有右子树时，就需要弹出下一个元素了
                else:
                    break
        return ans
    
    # ❌：这种遍历方式死循环
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = [root]
        ans = []
        while stk:
            if stk[-1].left: # 有左，就一直近作；但是父节点会重复访问，所以会无限循环
                stk.append(stk[-1].left)
                continue
            node = stk.pop()
            ans.append(node.val)
            if node.right:
                stk.append(node.right)
        return ans  