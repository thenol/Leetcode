'''
[medium]

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-query-mutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class NumArray:

    def __init__(self, nums: List[int]):
        self.n=len(nums)
        self.nums=nums
        self.arr=[0]*(self.n+1)
        for i in range(len(nums)):
            self.modify(i,nums[i])
        # print(self.arr)

    def update(self, i: int, val: int) -> None:
        self.modify(i,val-self.nums[i])
        self.nums[i]=val
        # print(i,val,self.arr)
        
    def modify(self,i:int,val:int)->None:
        i+=1
        while i<=self.n:
            self.arr[i]+=val
            i+=i&-i

    def acc(self,i):
        if i<0:
            return 0
        sm=0
        while i>=1:
            sm+=self.arr[i]
            i-=i&-i
        return sm

    def sumRange(self, i: int, j: int) -> int:                                  
        return self.acc(j+1)-self.acc(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)