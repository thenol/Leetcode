'''
Say you have an array for which the i-th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:

Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
Example 2:

Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # method 1:dfs (time limit exceeded)
        mx=0
        def dfs(prices,sm,level):
            nonlocal mx
            if not prices or level==0:
                mx=mx if mx>=sm else sm
            else:
                for i in range(len(prices)):
                    for j in range(i+1,len(prices)):
                        if prices[j]>prices[i]:
                            dfs(prices[j:],sm+prices[j]-prices[i],level-1)
                mx=mx if mx>=sm else sm
        dfs(prices,0,k)
        return mx



        # method 2: dynamic progrogramming with one dimension, which is wrong because the state is up to two dimension (location,k) or state collision. So it will override the previous value (e.g. <p,k> override the <p,k-1>)
        d=[0]+[-1 for _ in range(len(prices)-1)]
        def dp(p,k):
            if p>=0 and d[p]!=-1:
                return d[p]
            else:
                for i in range(p):
                    if prices[p]>prices[i]:
                        d[p]=max(max(dp(i,k-1)+prices[p]-prices[i],dp(i,k)),d[p])
                    else:
                        d[p]=max(dp(i,k),d[p])
                    print(d)
                return d[p]
        
        dp(len(prices)-1,k)
        print(d)
        return d[len(prices)-1]
        '''
        2
        [3,3,5,0,0,3,1,4]

        output:
            expected: 6
            result: 8 wrong
        '''
                    




        # method 2: dynamic programming with two factors (i.e. two dimension <loc,k>) (time limit exceeded)
        class Solution:
            def maxProfit(self, k: int, prices: List[int]) -> int:                    
                # method 2: dynamic programming with two factors (i.e. two dimension <loc,k>)
                if not prices or k==0:
                    return 0
                d=[[-1 for _ in range(k)] for _ in range(len(prices))]
                for i in range(k):
                    d[0][i]=0
                mn=prices[0]
                mx=0 # maximum profit
                for i in range(1,len(prices)):
                    if prices[i]>mn:
                        mx=mx if prices[i]-mn<=mx else prices[i]-mn
                    else:
                        mn=mn if prices[i]>=mn else prices[i]
                    d[i][0]=mx
                    
                def dp(p,k):
                    if p>=0 and k>=0:
                        # print(p,k)
                        if d[p][k]>=0:
                            return d[p][k]
                        else:
                            for i in range(p):
                                if prices[p]>prices[i]:
                                    # print(i,k-1)
                                    d[p][k]=max(max(dp(i,k-1)+prices[p]-prices[i],dp(i,k)),d[p][k])
                                else:
                                    d[p][k]=max(dp(i,k),d[p][k])
                            return d[p][k]
                dp(len(prices)-1,k-1)

                return d[len(prices)-1][k-1]


            


        