'''
[medium]
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
通过次数9,173提交次数14,476

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/super-ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# version 1: Priority Queue
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        from heapq import heappush,heappop
        pq=[1]
        s={1}
        while n>=1:
            ugly=heappop(pq)
            for i in primes:
                if i*ugly not in s:
                    heappush(pq,i*ugly)
                    s|={i*ugly}
            n-=1
        return ugly

# version 2: multiple pointers, similar to triple pointers
