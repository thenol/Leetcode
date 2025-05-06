'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 时间复杂度和空间复杂度都是 O(n^2)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder and inorder:
            node=TreeNode(preorder[0])
            for i in range(len(inorder)):
                if inorder[i]==preorder[0]:
                    break
            node.left=self.buildTree(preorder[1:i+1],inorder[:i])
            node.right=self.buildTree(preorder[i+1:],inorder[i+1:])
            return node
    
    # 时间复杂度 O(n)；空间复杂度 O(n)
    # 两个改进点：
    #   1. 查找下标，预处理成哈希
    #   2. 递归传递 区间左右端点，防止列表复制
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {x: i for i, x in enumerate(inorder)}

        def dfs(pre_l: int, pre_r: int, in_l: int, in_r: int) -> Optional[TreeNode]:
            if pre_l == pre_r:  # 空节点
                return None
            left_size = index[preorder[pre_l]] - in_l  # 左子树的大小
            left = dfs(pre_l + 1, pre_l + 1 + left_size, in_l, in_l + left_size)
            right = dfs(pre_l + 1 + left_size, pre_r, in_l + 1 + left_size, in_r)
            return TreeNode(preorder[pre_l], left, right)

        return dfs(0, len(preorder), 0, len(inorder))  # 左闭右开区间
