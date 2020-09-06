'''
[medium]
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

 

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
 

提示：

2 <= n <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# version 1: TLE O(n^3)
class Solution:
    def cuttingRope(self, n: int) -> int:
        # status: d[i][j] means maxiums product of i-j
        # equ: d[i][j]=max(d[i,k]*d[k+1][j],(k-i+1)*(j-k),d[i][j]) 剪2次+剪1次，易错点，剪一次的情况有好几种
        d=[[0 for _ in range(n)]for _ in range(n)]
        # initialization:
        for i in range(n):
            d[i][i]=1
        for le in range(2,n+1):
            for i in range(n-le+1):
                j=i+le-1 # i+le-1<n => i<n-le+1
                for k in range(i,j):
                    d[i][j]=max(d[i][k]*d[k+1][j],(k-i+1)*(j-k),d[i][j],d[i][k]*(j-k),(k-i+1)*d[k+1][j])
        return d[0][n-1]%(1000000000+7)



# version 2: AC O(n^2)
class Solution:
    def cuttingRope(self, n: int) -> int:
        # S: d[i] as the maximum value of length i
        # E: d[i]=max(d[j]*d[i-j],j*(i-j), d[j]*(i-j), j*d[i-j],d[i])
        #   剪2次及其以上：d[j]*d[i-j]
        #   剪1次及以上： j*(i-j), d[j]*(i-j), j*d[i-j]
        # 注意：不同的剪发，都要比较，要考虑齐全
        d=[0 for _ in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,i//2+1): # 可以减少重复计算d[5]:d[1-3]
                d[i]=max(d[j]*d[i-j],j*(i-j), d[j]*(i-j), j*d[i-j],d[i])
        return d[n]%(1000000000+7)
