'''
[middle,math]

Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once=twice=three=0
        for n in nums:
            twice|=once&n # 如果出现一次，就加到二次，否则二次集不变
            once^=n # 记录（如果出现两次，这一次就是第三次）or（如果没出现两次，这一次就是第一次）
            three=once&twice # 三次=出现两次之后，又出现了一次
            once&=~three # 把出现三次的从一次中抹去，只保留其他
            twice&=~three # 同上
        return once


# version 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        
        for num in nums:
            # first appearance: 
            # add num to seen_once 
            # don't add to seen_twice because of presence in seen_once
            
            # second appearance: 
            # remove num from seen_once 
            # add num to seen_twice
            
            # third appearance: 
            # don't add to seen_once because of presence in seen_twice
            # remove num from seen_twice
            seen_once = ~seen_twice & (seen_once ^ num) 
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once

# 作者：LeetCode
# 链接：https://leetcode-cn.com/problems/single-number-ii/solution/zhi-chu-xian-yi-ci-de-shu-zi-ii-by-leetcode/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。