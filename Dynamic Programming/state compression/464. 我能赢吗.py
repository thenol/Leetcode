"""
[meidum]

在 "100 game" 这个游戏中，两名玩家轮流选择从 1 到 10 的任意整数，累计整数和，先使得累计整数和 达到或超过  100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 不能 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 maxChoosableInteger （整数池中可选择的最大数）和 desiredTotal（累计和），若先出手的玩家能稳赢则返回 true ，否则返回 false 。假设两位玩家游戏时都表现 最佳 。

 

示例 1：

输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。
示例 2:

输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true
示例 3:

输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true
 

提示:

1 <= maxChoosableInteger <= 20
0 <= desiredTotal <= 300

https://leetcode.cn/problems/can-i-win/description/?source=vscode
"""
from functools import cache
from math import inf
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # 状态压缩dp 
        # state: d[state][desiredTotal] 表示 state中1都是被选择的，0还未选择，先手选择累加和为desiredTotal是否胜利
        # 0<=state<=2**20-1
        
        # initializaition
        ...

        # transition
        
        # WA
        # method 1: 错在哪呢：
        # ans = ans or f(state ^ (1<<(i-1)), cur-i) # f(state ^ (1<<(i-1)), cur-i) 后面这个已经是对手再决策了，但是却算到了自己的头上
        def f1(state, cur): # 一个函数怎么模拟出两个人的决策？
            """先手选择累加和为desiredTotal是否胜利"""
            if cur <= 0:
                return True
            
            ans = False
            mn = inf
            for i in range(maxChoosableInteger, 0, -1):
                # 注意：第0位表示1，也就是选择1，不需要移位
                # if (state >> (i-1)) ^ 1: # 易错点❌：不能用按位异或来检查某一位啊
                if (state >> (i-1)) & 1: # 正确的✅：必须按位与，这样除了最后一位，其他位都和0与掉了
                    # 选过了，跳过
                    continue 
                # 如果未选择，选择的情况下，想胜利
                mn = min(mn, i)
                ans = ans or f(state ^ (1<<(i-1)), cur-i)
            return ans if ans else f(state ^ (1<<(mn-1)), cur-mn) # 如果能赢最好；如果赢不了，也要给接下来的对手制造麻烦，也就是让他在做选择的时候，累积和最小，所以选一个最小的数

        # WA
        # method 2: 决策方式：每次为了累加和最低，都选择最小的
        # 但是这种方式其实不对，应该每次都选对方可能赢的，如果没有，就选择最小的
        def f2(state, cur): # 一个函数怎么模拟出两个人的决策？
            """先手选择累加和为desiredTotal是否胜利"""
            # ❗️这个时候可以理解为自己做决策
            if cur <= 0:
                return True
            
            ans = False
            mn = inf
            for i in range(maxChoosableInteger, 0, -1):
                # 注意：第0位表示1，也就是选择1，不需要移位
                # if (state >> (i-1)) ^ 1: # 易错点❌：不能用按位异或来检查某一位啊
                if (state >> (i-1)) & 1: # 正确的✅：必须按位与，这样除了最后一位，其他位都和0与掉了
                    # 选过了，跳过
                    continue 
                # 如果未选择，选择的情况下，想胜利
                mn = min(mn, i)
                if cur-i<=0: return True
            # 如果能赢最好；如果赢不了，也要给接下来的对手制造麻烦，也就是让他在做选择的时候，累积和最小，所以选一个最小的数
            # 如果下一步对手先手赢了，自己输
            # 如果下一步对手先手输了，自己赢
            return not f2(state ^ (1<<(mn-1)), cur-mn) # ❗️这个时候已经是对手在做决策了

        # WA
        @cache
        def f3(state, cur): #
            """先手选择累加和为desiredTotal是否胜利
            理性决策：
                1. 挨个检测自己选择某个数后，看对手在这种情况下先手决策的结果：
                    a. 如果任何情况下对手都赢，那么自己铁定输了
                    b. 如果有一种情况下，对手输了，那自己肯定就选择这个数
            """
            if cur <= 0:
                return True
            
            ans = False
            for i in range(1, maxChoosableInteger+1):
                # 注意：第0位表示1，也就是选择1，不需要移位
                # if (state >> (i-1)) ^ 1: # 易错点❌：不能用按位异或来检查某一位啊
                if (state >> (i-1)) & 1: # 正确的✅：必须按位与，这样除了最后一位，其他位都和0与掉了
                    # 选过了，跳过
                    continue 
                # 判断假设自己选择了当前数i，看看对手的结果,
                ans = ans or not f3(state ^ (1<<(i-1)), cur-i) # 如果有一次对手败了，自己就赢了，否则对手每种情况下都赢，自己铁定失败了
                if ans and state==0:
                    print(bin(state), i, cur, f3(state ^ (1<<(i-1)), cur-i))
            return ans

        # WA
        @cache
        def f5(state, cur): #
            """先手选择累加和为desiredTotal是否胜利
            理性决策：
                1. 挨个检测自己选择某个数后，看对手在这种情况下先手决策的结果：
                    a. 如果任何情况下对手都赢，那么自己铁定输了
                    b. 如果有一种情况下，对手输了，那自己肯定就选择这个数
            """
            # 这个地方其实是对手赢了，因为自己根本没有做任何决策
            # if cur <= 0:
            #     return True
            
            ans = True 
            for i in range(1, maxChoosableInteger+1):
                # 注意：第0位表示1，也就是选择1，不需要移位
                # if (state >> (i-1)) ^ 1: # 易错点❌：不能用按位异或来检查某一位啊
                if (state >> (i-1)) & 1: # 正确的✅：必须按位与，这样除了最后一位，其他位都和0与掉了
                    # 选过了，跳过
                    continue 
                # 判断假设自己选择了当前数i，看看对手的结果,
                if cur-i <=0 : return True # 赢了
                # 当对手在所有可能情况下都输的时候，才会承认自己赢，否则肯定对手赢了
                # 上述逻辑错误❌：先手情况下，先下手为强，自己能赢，不一定所有情况下对手都会输，体现先手条件的重要性
                ans = ans and not f5(state ^ (1<<(i-1)), cur-i) 

                # if ans and state==0:
                #     print(bin(state), i, cur, f4(state ^ (1<<(i-1)), cur-i))
            return ans
        
        # ++++++++++++++++ AC +++++++++++++++++
        @cache
        def f4(state, cur): #
            """先手选择累加和为desiredTotal是否胜利
            理性决策：
                1. 挨个检测自己选择某个数后，看对手在这种情况下先手决策的结果：
                    a. 如果任何情况下对手都赢，那么自己铁定输了
                    b. 如果有一种情况下，对手输了，由于自己在先手情况下有优势，一定会选择这个让自己赢的数
                注意：
                    自己赢不意味着对手在每种情况下都会输，由于有先手优势，所以自己才能先寻找自己赢的机会，一旦找到就赢了；否则，所有情况都找过了，都赢不了，那么只能输给对手
            """
            # 这个地方其实是对手赢了，因为自己根本没有做任何决策
            # if cur <= 0:
            #     return True

            # 如果本身情况不合法，则不可能成功
            if (1+maxChoosableInteger)*maxChoosableInteger//2 < desiredTotal:
                return False

            ans = False 
            for i in range(1, maxChoosableInteger+1):
                # 注意：第0位表示1，也就是选择1，不需要移位
                # if (state >> (i-1)) ^ 1: # 易错点❌：不能用按位异或来检查某一位啊
                if (state >> (i-1)) & 1: # 正确的✅：必须按位与，这样除了最后一位，其他位都和0与掉了
                    # 选过了，跳过
                    continue 
                # 判断假设自己选择了当前数i，看看对手的结果,
                if cur-i <=0 : return True # 赢了
                # 如果有一次对手败了，自己就赢了，❗️因为自己是先手❗️，理性决策一定会抓住机会，否则如果对手抓住了先手赢的机会，对手就赢了
                # 因此，自己检查每种情况，有一种情况赢了，就赢了
                ans = ans or not f4(state ^ (1<<(i-1)), cur-i) 
                # if ans and state==0:
                #     print(bin(state), i, cur, f4(state ^ (1<<(i-1)), cur-i))
            return ans
        
        return f4(0, desiredTotal)

        # ++++++++++++++++ AC +++++++++++++++++
