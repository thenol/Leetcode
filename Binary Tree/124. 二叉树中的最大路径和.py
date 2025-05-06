"""
[hard]

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

 

示例 1：


输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
示例 2：


输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
 

提示：

树中节点数目范围是 [1, 3 * 104]
-1000 <= Node.val <= 1000

https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
相似题：543. 二叉树的直径

思路：
    链：从下面的某个节点（不一定是叶子）到当前节点的路径。把这条链的节点值之和，作为 dfs 的返回值。如果节点值之和是负数，则返回 0。
    
    直径：等价于由两条（或者一条）链拼成的路径。我们枚举每个 node，假设直径在这里「拐弯」，也就是计算由左右两条从下面的某个节点（不一定是叶子）到 node 的链的节点值之和，去更新答案的最大值。

⚠注意：dfs 返回的是链的节点值之和，不是直径的节点值之和。

https://leetcode.cn/problems/binary-tree-maximum-path-sum/solutions/2227021/shi-pin-che-di-zhang-wo-zhi-jing-dpcong-n9s91/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node: Optional[TreeNode]) -> int: # 返回节点最大链和
            if node is None:
                return 0  # 没有节点，和为 0
            l_val = dfs(node.left)  # 左子树最大链和
            r_val = dfs(node.right)  # 右子树最大链和
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)  # 两条链拼成路径；遍历经过所有节点的直径之和
            return max(max(l_val, r_val) + node.val, 0)  # 当前子树最大链和（注意这里和 0 取最大值了）；默认情况下最小是0
        dfs(root)
        return ans
