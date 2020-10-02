'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

#
# 
# @param array int整型一维数组 
# @return int整型一维数组
#

# version 1: WA，不稳定，in-place
'''
class Solution:
    def reOrderArray(self , array ):
        # write code here
        i,j=0,-1
        n=len(array)
        while i<n and j<n:
            if array[i]%2==0:
                if j==-1:
                    j=i+1
                while j<n and array[j]%2==0:
                    j+=1
                if j==n: #对j操作，就得对j做边界检查
                    return array
                array[i],array[j]=array[j],array[i]
            i+=1
        return array
'''

# version 2: O(n)，no offer
arr1=[odd]
arr2=[even]
arr3=arr1+arr2

# version 3: in-place, O(n^2)





