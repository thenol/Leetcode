"""
[medium]

有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。

最开始时：

「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；
「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。
「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。

之后两位玩家轮流进行操作，「一号」玩家先手。每一回合，玩家选择一个被他染过色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色（「一号」玩家染红色，「二号」玩家染蓝色）。

如果（且仅在此种情况下）当前玩家无法找到这样的节点来染色时，其回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true ；若无法获胜，就请返回 false 。

 
示例 1 ：


输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：true
解释：第二个玩家可以选择值为 2 的节点。
示例 2 ：

输入：root = [1,2,3], n = 3, x = 1
输出：false
 

提示：

树中节点数目为 n
1 <= x <= n <= 100
n 是奇数
1 <= Node.val <= n
树中所有值 互不相同

https://leetcode.cn/problems/binary-tree-coloring-game/description/?source=vscode
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 更简洁写法
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        lsz = rsz = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            ls = dfs(node.left)
            rs = dfs(node.right)
            if node.val == x:
                nonlocal lsz, rsz
                lsz, rsz = ls, rs
            return ls + rs + 1
        dfs(root)
        return max(lsz, rsz, n - 1 - lsz - rsz) * 2 > n


    # method 2: 树型dp
    # 核心思路【充要条件】：类似围棋，选择x周围任意一种可能，如果可以赢，就肯定能赢
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def f(node, e):
            """返回node上e的子节点个数"""
            nonlocal n
            if not node: return (
                0, # 找到的e的子节点个数
                0, # node 子节点总数
                False, # 是否能赢
                ) 
            cnt1, child1, w1 = f(node.left, e)
            cnt2, child2, w2 = f(node.right, e)
            all_child = child1 + child2 + 1
            all_cnt = cnt1 + cnt2
            ans = False
            if node.val == e:
                # 二手选择涂父节点
                ans = ans or all_child<n-all_child

                # 二手选择涂左节点
                ans = ans or n-child1<child1

                # 二手选择涂右节点
                ans = ans or n-child2<child2
                
                return all_child, all_child, ans or w1 or w2
            else:
                return all_cnt, all_child, ans or w1 or w2
        return f(root, x)[2]

    # method 1: 本质上就是在求x的子节点的个数
    # 错在子节点可选——即只考虑了一种情况，就是涂父节点的情况
    # ❌WA: 反例——[1,2,3,4,5]\n5\n1
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        def f(node, e):
            """返回node上e的子节点个数"""
            if not node: return (0, 0) # (e子节点个数，当前node总节点数)
            cnt1, child1 = f(node.left, e)
            cnt2, child2 = f(node.right, e)
            all_child = child1 + child2 + 1
            all_cnt = cnt1 + cnt2
            if node.val == e:
                return all_child, all_child
            else:
                return all_cnt, all_child
        ans = f(root, x)[0]
        print(ans)
        return ans < n-ans
      