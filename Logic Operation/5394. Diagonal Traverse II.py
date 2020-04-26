'''
Given a list of lists of integers, nums, return all elements of nums in diagonal order as shown in the below images.
 

Example 1:



Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,4,2,7,5,3,8,6,9]
Example 2:



Input: nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
Output: [1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]
Example 3:

Input: nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
Output: [1,4,2,5,3,8,6,9,7,10,11]
Example 4:

Input: nums = [[1,2,3,4,5,6]]
Output: [1,2,3,4,5,6]
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i].length <= 10^5
1 <= nums[i][j] <= 10^9
There at most 10^5 elements in nums.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diagonal-traverse-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic={}
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                row=i if j==0 else j+i
                if row in dic:
                    dic[row].append(nums[i][j])
                else:
                    dic[row]=[nums[i][j]]
                # print(dic)
        ans=[]
        for k,v in dic.items():
            ans+=v[::-1]
        return ans


# save the elements in the same diagonal line to the same row, whose number equals i+j