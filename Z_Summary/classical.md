### Backtrack
* [494]目标和
* [3393]统计异或值为给定值的路径数目

### Bin search
* [410]分割数组的最大值
* [1004]最大连续1的个数 III (二分和滑动窗口解法)
* [3399]字符相同的最短子字符串 II
* [3419]图的最大边权的最小值

### Contribution
* [3428]最多 K 个元素的子序列的最值之和

### Digitial dp
* [78]子集
* [357]统计各位数字都不同的数字个数
* [600]不含连续1的非负整数
* [902]最大为 N 的数字组合
* [967]连续差相同的数字

### Graph
* [909]蛇梯棋
* [934]最短的桥
* [1020]飞地的数量
* [1053]交换一次的先前排列
* [1081]不同字符的最小子序列
* [1129]颜色交替的最短路径
* [3435]最短公共超序列的字母出现频率

### Greedy
* [321]拼接最大数
* [517]超级洗衣机
* [1024]视频拼接
* [1163]按字典序排在最后的子串
* [3397]执行操作后不同元素的最大数量
* [3403]从盒子中找出字典序最大的字符串 I

### Interval dp <a href="https://leetcode.cn/problems/remove-boxes/solutions/1884753/by-424479543-g3gt/?source=vscode">🪝</a>
* [312]戳气球
* [87]扰乱字符串
* [375]猜数字大小 II
* [730]统计不同回文子序列
* **prefix or suffix**
    * [546]移除盒子
    * [664]奇怪的打印机
* [1000]合并石头的最低成本
* [1130]叶值的最小代价生成树

### Knapsack
* **complete knapsack**
* **01 knapsack**
    * [474]一和零
    * [629]K 个逆序对数组
    * [689]三个无重叠子数组的最大和
    * [923]三数之和的多种可能 (三位数组内存优化)
    * [956]最高的广告牌
    * [3414]不重叠区间的最大得分
* **complete knapsack**
    * [638]大礼包

### Linear
* [514]自由之路
* [639]解码方法 II
* [741]摘樱桃
* [980]不同路径 III

### Math
* **congruence**
    * [523]连续的子数组和
    * [3381]长度可被 K 整除的子数组的最大元素和
* **combination**
    ```python3
    from math import comb # 求组合数
    ```
    * [3395]唯一中间众数子序列 I
    * [3405]统计恰好有 K 个相等相邻元素的数组数目
    * [3426]所有安放棋子方案的曼哈顿距离
* [1042]不邻接植花
* [3411]最长乘积等价子数组

### Operator
* [1017]负二进制转换

### Prefix and Suffix
* Prefix sum
    * [363]矩形区域不超过 K 的最大数值和
    * [467]环绕字符串中唯一的子字符串
* [3404]统计特殊子序列的数目
* [3410]删除所有值为某个元素后的最大子数组和

### Sliding window
* [239]滑动窗口最大值 —— 单调队列
* [2271]毯子覆盖的最多白色砖块数
* [3420]统计 K 次操作以内得到非递减子数组的数目
* [3425]最长特殊路径
* [3439]重新安排会议得到最多空余时间 I
* [3440]重新安排会议得到最多空余时间 II

### Stack
* [1111]有效括号的嵌套深度
* [3412]计算字符串的镜像分数

### State compression
* [464]我能赢吗 (❗️注意结算时间)
* [486]预测赢家
* [691]贴纸拼词
* [698]划分为k个相等的子集

### State matchine
* [3434]子数组操作后的最大频率

### String
* **next table**
    * [466]统计重复个数
* **Trie Tree**
    * [472]连接词

### Subsequence
* **Continuous**
    * [32]最长有效括号
    * [413]等差数列划分
    * [446]等差数列划分II
    * [718]最长重复子数组
* **Interleaved**
    * [368]最大整除子集
    * [514]自由之路
    * [650]两个键的键盘
    * [188]买卖股票的最佳时机 IV
    * [198]打家劫舍 (注意本质与隔一天买卖股票一样)
    * [740]删除并获得点数
    * [769]最多能完成排序的块
    * [3409]最长相邻绝对差递减子序列 (状态中有一个纬度表示范围)
* **LIS**
    * [354]俄罗斯套娃信封问题
    * [673]最长递增子序列的个数
* **String**
    * [712]两个字符串的最小ASCII删除和

### Sweep Line
* [3382]用点构造面积最大的矩形 II

### Tree
* [95]不同的二叉搜索树II 
    $$\begin{align*}&G(n+1) = \frac{\color{red}G(n)*(4n+2)}{n+2};\\&catlan = \frac{1}{n+1}C_{2n}^n\\&1. n=0，G(0)=1\\&2.n>=1时，G(n+1) = (4n+2)*G(n)/(n+2);\end{align*}$$
* [1130]叶值的最小代价生成树

### Tree DP
* [1145]二叉树着色游戏

### Union
* [803]打砖块


### 数据结构
* Trie
* Fenwick Tree
* Segment Tree
* Union Set