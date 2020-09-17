'''
[medium]
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。

示例 1：

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1
示例 2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
提示：

2 <= n <= 58
注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jian-sheng-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def cuttingRope(self, n: int) -> int:
        # S: d[i] as max value of length-i
        # E: d[i]=max(d[i-j]*d[j],(i-j)*j,d[i-j]*j,(i-j)*d[j])
        # init: d[1]=1,d[2]=1,d[3]=2
        d=[1 for _ in range(n+1)]
        d[1]=d[2]=1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                d[i]=max(d[i-j]*d[j],(i-j)*j,d[i-j]*j,(i-j)*d[j],d[i]) #别忘了更新自己
        return d[n]
