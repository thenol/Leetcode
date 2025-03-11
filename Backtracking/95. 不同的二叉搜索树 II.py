"""
[medium]

给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

 

示例 1：


输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 8

https://leetcode.cn/problems/unique-binary-search-trees-ii/description/
"""

# 树类问题的通解——回溯：分而治之 
# 将树拆解为：左子树+根节点+右子树
# 分别就子树进行创建，最后组合成树即可

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def tree(nodes):
            """
            创建节点为nodes的所有排序树
            """
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
                        # 遍历创建的所有左子树，右子树，然后组合，添加到结果集中
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
