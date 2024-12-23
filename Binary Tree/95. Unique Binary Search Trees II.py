'''
[medium]

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def tree(nodes):
            """输入节点列表[]返回所有可能的树"""
            if not nodes: return [None] # 默认为空, 加入哨兵，可以让下面遍历成立，从而不用检测左右子树是否存在
            ans = []
            for i in range(len(nodes)):
                left = tree(nodes[:i]) # 递归遍历左子树
                right = tree(nodes[i+1:]) # 右子树
                for l in left:
                    for r in right:
                        p = TreeNode(nodes[i])
                        p.left = l
                        p.right = r
                        ans.append(p)
            
            return ans
        
        nodes = list(range(1, n+1))
        return tree(nodes)

    def generateTrees(self, n: int) -> List[TreeNode]:
        def tree(nodes):
            if not nodes:
                return [None]
            elif len(nodes)==1:
                return [TreeNode(nodes[0])]
            res=[]
            for i in range(len(nodes)):
                left=tree(nodes[:i])
                right=tree(nodes[i+1:])
                # print(left,right)
                for l in left:
                    for r in right:
                        if l or r:
                            node=TreeNode(nodes[i])
                            node.left=l
                            node.right=r
                            res.append(node)
            return res
        if not n:
            return []
        nodes=[_ for _ in range(1,n+1)]
        ret=[]
        ret+=tree(nodes)
        return ret

# 所谓优化，都是为了避免重复计算，而本质就是遍历计算所有情况