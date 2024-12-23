'''
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。

 

参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true
 

提示：

数组长度 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder)<=2:return True
        root=postorder[-1]
        pivot=False
        for i in range(len(postorder)):
            if postorder[0]<root:
                if postorder[i]>=root and not pivot:
                    pivot=i
                elif pivot and postorder[i]<root:
                    return False
            elif postorder[0]>root:
                if postorder[i]<root:
                    return False
                else:
                    pivot=i
        # print(postorder[:pivot],postorder[pivot:len(postorder)-1])
        return self.verifyPostorder(postorder[:pivot]) and self.verifyPostorder(postorder[pivot:len(postorder)-1])   
