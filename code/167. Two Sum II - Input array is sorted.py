'''
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={v:k for k,v in enumerate(numbers)}
        # print(dic)
        N=len(numbers)
        idx=0
        for i in range(N):
            if target-numbers[i] in dic and target-numbers[i]!=numbers[i]:
                return [i+1,dic[target-numbers[i]]+1]
            elif target-numbers[i]==numbers[i]:
                idx=i

        return [idx,idx+1]