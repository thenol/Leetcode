"""
[medium]

给你一个二维整数数组 tiles ，其中 tiles[i] = [li, ri] ，表示所有在 li <= j <= ri 之间的每个瓷砖位置 j 都被涂成了白色。

同时给你一个整数 carpetLen ，表示可以放在 任何位置 的一块毯子的长度。

请你返回使用这块毯子，最多 可以盖住多少块瓷砖。

 

示例 1：



输入：tiles = [[1,5],[10,11],[12,18],[20,25],[30,32]], carpetLen = 10
输出：9
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 9 块瓷砖，所以返回 9 。
注意可能有其他方案也可以覆盖 9 块瓷砖。
可以看出，瓷砖无法覆盖超过 9 块瓷砖。
示例 2：



输入：tiles = [[10,11],[1,1]], carpetLen = 2
输出：2
解释：将毯子从瓷砖 10 开始放置。
总共覆盖 2 块瓷砖，所以我们返回 2 。
 

提示：

1 <= tiles.length <= 5 * 104
tiles[i].length == 2
1 <= li <= ri <= 109
1 <= carpetLen <= 109
tiles 互相 不会重叠 。

https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/description/

"""

"""
最优解法：https://leetcode.cn/problems/maximum-white-tiles-covered-by-a-carpet/solutions/1496434/by-endlesscheng-kdy9/
# 核心思路： 排序 + 滑动窗口
#     * 【推理过程】
#         <= 解一定包含所有可能性
          <= 由提示知道 O(N) 或者 O(NlogN) 解法
          <= 如果是 O(N) 解法，则主循环遍历 1 次
          <= 滑动窗口，但是无法缓存，因为数据量太大；同样也无法直接遍历所有区间，因为数据量太大
          <= 显然，只能遍历所有区间，寻找等价条件
#     * 【条件转化】
          <= 实际上，毯子右端点放在一段瓷砖中间，是不如直接放在这段瓷砖右端点的（因为从中间向右移动，能覆盖的瓷砖数不会减少），所以可以枚举每段瓷砖的右端点来摆放毯子的右端点或者左端点。

      * 【归纳总结】
          <= 排序 + 区间层面的滑动窗口
"""

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # 首先将瓷砖区间按照起始位置进行排序
        tiles.sort(key=lambda x: x[0])
        
        # 初始化变量：
        # ans: 最终结果，表示最大覆盖的瓷砖数
        # cover: 当前滑动窗口内覆盖的瓷砖数
        # left: 滑动窗口的左边界
        ans = cover = left = 0
        
        # 遍历每个瓷砖区间
        for tl, tr in tiles:
            # 将当前瓷砖的长度加入到覆盖范围中
            cover += tr - tl + 1 # 滑动窗口累加
            
            # 情况一：覆盖单一区间瓷砖
            # 如果滑动窗口的左边界瓷砖的右端点已经超出了当前滑动窗口的覆盖范围
            # 则需要将左边界向右移动，并减少覆盖范围
            while tiles[left][1] < tr - carpetLen + 1: # ❗️将当前不在窗口内的区间移出❗️
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            
            # ❗️处理区间右端点仍然在窗口内的情况❗️
            # 情况二：覆盖多个区间瓷砖，但是覆盖不全
            # 计算未覆盖的部分（即滑动窗口左侧未完全覆盖的部分）
            uncover = max(tr - carpetLen + 1 - tiles[left][0], 0)
            
            # 更新最大覆盖的瓷砖数
            ans = max(ans, cover - uncover)
        
        # 返回最终结果
        return ans