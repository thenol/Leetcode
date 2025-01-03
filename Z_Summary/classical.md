### Knapsack
* **complete knapsack**
* **01 knapsack**
    * [474]一和零
    * [629]K 个逆序对数组
    * [689]三个无重叠子数组的最大和
* **complete knapsack**
    * [638]大礼包

### Interval dp <a href="https://leetcode.cn/problems/remove-boxes/solutions/1884753/by-424479543-g3gt/?source=vscode">🪝</a>
* [312]戳气球
* [87]扰乱字符串
* [375]猜数字大小 II
* [730]统计不同回文子序列
* **prefix or suffix**
    * [546]移除盒子
    * [664]奇怪的打印机

### Digitial dp
* [357]统计各位数字都不同的数字个数
* [600]不含连续1的非负整数
* [902]最大为 N 的数字组合

### Greedy
* [321]拼接最大数
* [517]超级洗衣机
* [3397]执行操作后不同元素的最大数量

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
* **LIS**
    * [354]俄罗斯套娃信封问题
    * [673]最长递增子序列的个数
* **String**
    * [712]两个字符串的最小ASCII删除和

### Linear
* [514]自由之路
* [639]解码方法 II
* [741]摘樱桃

### Tree
* [95]不同的二叉搜索树II 
    $$\begin{align*}&G(n+1) = \frac{\color{red}G(n)*(4n+2)}{n+2};\\&catlan = \frac{1}{n+1}C_{2n}^n\\&1. n=0，G(0)=1\\&2.n>=1时，G(n+1) = (4n+2)*G(n)/(n+2);\end{align*}$$
    ```python3
    from math import comb # 求组合数
    ```

### Prefix sum
* [363]矩形区域不超过 K 的最大数值和
* [467]环绕字符串中唯一的子字符串

### Bin search
* [410]分割数组的最大值

### State compression
* [464]我能赢吗 (❗️注意结算时间)
* [486]预测赢家
* [691]贴纸拼词
* [698]划分为k个相等的子集

### Sliding window


### String
* **next table**
    * [466]统计重复个数
* **Trie Tree**
    * [472]连接词

### Sweep Line
* [3382]用点构造面积最大的矩形 II

### Backtrack
* [3393]统计异或值为给定值的路径数目
* [494]目标和

### Math
* **congruence**
    * [523]连续的子数组和
    * [3381]长度可被 K 整除的子数组的最大元素和
* **combination**
    * [3395]唯一中间众数子序列 I

### Union
* [803]打砖块

### 数据结构
* Trie
* Fenwick Tree
* Segment Tree
* Union Set