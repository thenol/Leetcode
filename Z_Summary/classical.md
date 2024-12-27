### knapsack
* **complete knapsack**
* **01 knapsack**
    * [474]一和零
    * [629]K 个逆序对数组 （多归约态）
* **complete knapsack**
    * [638]大礼包 (一般都需要**转换**问题)

### <a href="https://leetcode.cn/problems/remove-boxes/solutions/1884753/by-424479543-g3gt/?source=vscode">interval dp</a>
* [312]戳气球
* [87]扰乱字符串
* [375]猜数字大小 II
* [546]移除盒子

### digitial dp
* [357]统计各位数字都不同的数字个数
* [600]不含连续1的非负整数

### greedy
* [321]拼接最大数
* [517]超级洗衣机

### subsequence
* **Continuous**
    * [32]最长有效括号
    * [413]等差数列划分
    * [446]等差数列划分II
* **Interleaved**
    * [368]最大整除子集
    * [514]自由之路
* **LIS**
    * [354]俄罗斯套娃信封问题

### linear
* [514]自由之路

### tree
* [95]不同的二叉搜索树II 
    $$\begin{align*}&G(n+1) = \frac{\color{red}G(n)*(4n+2)}{n+2};\\&catlan = \frac{1}{n+1}C_{2n}^n\\&1. n=0，G(0)=1\\&2.n>=1时，G(n+1) = (4n+2)*G(n)/(n+2);\end{align*}$$
    ```python3
    from math import comb # 求组合数
    ```

### prefix sum
* [363]矩形区域不超过 K 的最大数值和
* [467]环绕字符串中唯一的子字符串

### bin search
* [410]分割数组的最大值

### state compression
* [464]我能赢吗 (❗️注意结算时间)
* [486]预测赢家

### sliding window


### string
* **next table**
    * [466]统计重复个数
* **Trie Tree**
    * [472]连接词

### sweep Line
* [3382]用点构造面积最大的矩形 II

### backtrack
* [3393]统计异或值为给定值的路径数目
* [494]目标和

### math
* **congruence**
    * [523]连续的子数组和
    * [3381]长度可被 K 整除的子数组的最大元素和
* **combination**
    * [3395]唯一中间众数子序列 I