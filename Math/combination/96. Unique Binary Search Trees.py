'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# 思路：卡特兰数
"""
推导过程：

1. 假设 n 个节点存在二叉排序树的个数为 G(n)，令 f(i) 为以 i 为根的二叉搜索排序树的个数，则
G(n) = f(1) + f(2) + ... + f(n)

2. 当 i 为根节点时，其左子树节点个数为 i-1 个，右子树节点为 n-i，则
f(i) = G(i-1)*G(n-i)

综上得：
G(n) = G(0)*G(n-1) + G(1)*G(n-2) + ... + G(n-1)*G(0)

得
G(n) = C_(2n)^(n)/(n+1)

1. n=0，G(0)=1
2. n>=1时，G(n+1) = [(4n+2)/(n+2)] * G(n); 
"""
class Solution:
    def numTrees(self, n: int) -> int:
        f=lambda n,pre: (2*(2*n+1)/(n+2))*pre
        pre=1
        for i in range(n):
            pre=f(i,pre)
        return int(pre)