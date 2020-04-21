'''
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# from math import sqrt
# class Solution:
#     def countPrimes(self, n: int) -> int:
#         def isPrime(N):
#             for i in range(2,int(sqrt(N))+1):
#                 if N%i==0:
#                     return False
#             return True
        
#         count=0
#         # ans=[]
#         for i in range(2,n):
#             if isPrime(i):
#                 count+=1
#                 # ans.append(i)
#         # print(ans)
#         return count


# Euler sieve
class Solution:
    def countPrimes(self, n: int) -> int:
        nums=[True]*(n+1)
        primes=[] # ascending
        for i in range(2,n):
            if nums[i]:
                primes.append(i)
            for j in range(len(primes)):
                if i*primes[j]>n:
                    break
                nums[i*primes[j]]=False
                if (i%primes[j])==0:
                    break
        return len(primes)
