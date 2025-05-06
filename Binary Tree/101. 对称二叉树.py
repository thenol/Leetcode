"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false
 

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100
 

进阶：你可以运用递归和迭代两种方法解决这个问题吗？

https://leetcode.cn/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-100-liked
"""

"""
思路：
    将对称的两个节点，同时放入队列中，

https://leetcode.cn/problems/symmetric-tree/solutions/46560/dong-hua-yan-shi-101-dui-cheng-er-cha-shu-by-user7/?envType=study-plan-v2&envId=top-100-liked
"""

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root or not (root.left or root.right):
			return True
		# 用队列保存节点	
		queue = [root.left,root.right]
		while queue:
			# 从队列中取出两个节点，再比较这两个节点
			left = queue.pop(0)
			right = queue.pop(0)
			# 如果两个节点都为空就继续循环，两者有一个为空就返回false
			if not (left or right):
				continue
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			# 将左节点的左孩子， 右节点的右孩子放入队列
			queue.append(left.left)
			queue.append(right.right)
			# 将左节点的右孩子，右节点的左孩子放入队列
			queue.append(left.right)
			queue.append(right.left)
		return True
