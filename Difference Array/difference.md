# 差分数组
## 一维差分

### 举例
考虑数组 $a=[1,3,3,5,8]$，对其中的相邻元素两两作差（右边减左边），得到数组 $[2,0,2,3]$。然后在开头补上 $a[0]$，得到差分数组

$$d=[1,2,0,2,3]$$
这有什么用呢？如果从左到右累加 $d$ 中的元素，我们就「还原」回了 $a$ 数组 $[1,3,3,5,8]$。这类似求导与积分的概念。

这又有什么用呢？现在把连续子数组 $a[1],a[2],a[3]$ 都加上 10，得到 $a^′=[1,13,13,15,8]$。再次两两作差，并在开头补上 $a^′[0]$，得到差分数组
$$ d^′=[1,12,0,2,−7] $$
对比 $d$ 和 $d^′$，可以发现只有 $d[1]$ 和 $d[4]$ 变化了，这意味着对 $a$ 中连续子数组的操作，可以转变成对差分数组 $d$ 中两个数的操作。

### 定义和性质
对于数组 a，定义其**差分数组**（difference array）为
$$

d[i] =
\left\{
\begin{array}{ll}
a[0] & \text{if } i = 0, \\
a[i]-a[i-1] & \text{if } i \geq 0.
\end{array}
\right.

​$$
 
* **性质 1**：从左到右累加 $d$ 中的元素，可以得到数组 $a$。

* **性质 2**：如下两个操作是等价的。
    * 把 a 的子数组 $a[i],a[i+1],…,a[j]$ 都加上 $x$。
    *  把 $d[i]$ 增加 $x$，把 $d[j+1]$ 减少 $x$。

    利用性质 2，我们只需要 $O(1)$ 的时间就可以完成对 a 的子数组的操作。最后利用性质 1 从差分数组复原出数组 a。

注：也可以这样理解，$d[i]$ 表示把下标 $≥i$ 的数都加上 $d[i]$。


## 二维度差分
<img src='../Z_Summary/resources/difference.png'>


### references
> 一维差分：https://leetcode.cn/problems/car-pooling/solutions/2550264/suan-fa-xiao-ke-tang-chai-fen-shu-zu-fu-9d4ra/

> 二维差分：https://leetcode.cn/problems/stamping-the-grid/solutions/1199642/wu-nao-zuo-fa-er-wei-qian-zhui-he-er-wei-zwiu/