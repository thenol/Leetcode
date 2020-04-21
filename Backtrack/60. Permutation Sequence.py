'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res=[]
        def dfs(nums,path):
            nonlocal k
            # print(nums,k)
            if not nums:
                # print(path,k)
                if k==1:
                    res.append(path)
                k-=1
                return
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:],path+[str(nums[i])])
                if k<=0:
                    break
        i,unit=1,1
        while i<=n-1:
            unit*=i
            i+=1
        nums=[_ for _ in range(1,n+1)]

        # ------------------------------------------------------------- #

        first=(k-1)//unit 
        k=(k-1)%unit+1

        # comment: the beauty of the unit
        # when first=k//unit:
        '''
         the sequence is below: k=3,n=3, nums=[1,2,3], unit=2
         k unit first
         1  2   0
         2  2   1
         3  2   1
         4  2   2
         5  2   2
         ，，， 

         so, if you want the sequence start from double zero, you can set k to k-1


        k%unit
        k unit k%unit
        1   2   1
        2   2   0
        3   2   1
        4   2   0
        5   2   1

        on the other hand, you can also set k to k-1 to implement the value of k%unit starts from zero

        '''


        # ------------------------------------------------------------- #
        
        
        # print(first,nums[first],nums[:first]+nums[first+1:])
        dfs(nums[:first]+nums[first+1:],[str(nums[first])])
        # print(res)
        return ''.join(res[0])


