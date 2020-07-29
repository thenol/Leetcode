'''
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class NumArray:
    nums=[]
    def __init__(self, nums: List[int]):
        acc=0
        for i in range(len(nums)):
            acc+=nums[i]
            self.nums.append(acc)
        self.nums.append(0)

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j]-self.nums[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)