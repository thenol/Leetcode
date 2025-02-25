# 常用函数

* 查找
  * 二分查找：需要关注查找成功情况下的坐标范围 **[0,n)** 和查找失败时的下标 **{-1, n}**
    ```python
    #https://blog.csdn.net/YMWM_/article/details/122378152
    #bisect.bisect和bisect.bisect_right返回大于x的第一个下标(相当于C++中的upper_bound)，bisect.bisect_left返回大于等于x的第一个下标(相当于C++中的lower_bound)。
      import bisect
      ls = [1,5,9,13,17]
      index1 = bisect.bisect(ls,9)
      index2 = bisect.bisect_left(ls,9)
      index3 = bisect.bisect_right(ls,9)
      print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
      #index1 = 3, index2 = 2, index3 = 3
      
      # 函数声明：
      #   1. key的作用：对序列 a 中的每个元素调用 key 函数，并根据返回值进行比较。如果提供了 key，则 x 也会被 key 处理后再进行比较。
      bisect_left(a, x, lo=0, hi=len(a), key=None)
      # 例如：bisect_left(range(max_w + 1), True, 1, key=check)
      # 含义：在 range(max_w + 1) 中，查找范围的起始索引是 1，找到第一个使得 check(w) 返回 True 的权重值 w。
      """
      假设 max_w = 5，range(max_w + 1) 是 [0, 1, 2, 3, 4, 5]，并且 check 函数的返回值如下：
      check(0) = False => 0
      check(1) = False => 0
      check(2) = True => 1
      check(3) = True => 1
      check(4) = True => 1
      check(5) = True => 1
      那么 bisect_left(range(max_w + 1), True, 1, key=check) 会返回 2，因为 2 是第一个使得 check(w) 返回 True 的权重值。
      """
    ```

* 循环理解
  ```python
    while 0<=i and left <= s_c[i][1]: # 隐藏哨兵左护法，默认不等；换句话说，循环一直执行当[0,...]范围内left <= s_c[j][1]成立；而退出循环时，即为不成立left > s_c[j][1]
      i -= 1
      left_most = min(left_most, s_c[i][0])
  ```
* deque: 全称为 "double-ended queue"，即双端队列
  ```python
  from collections import deque

  # 创建一个空的deque
  d = deque()

  # 向deque中添加元素
  d.append('a')  # 在右侧添加
  d.append('b')
  d.append('c')

  d.appendleft('x')  # 在左侧添加
  d.appendleft('y')

  # 从deque中弹出元素
  print(d.pop())  # 输出：'c'，从右侧弹出
  print(d.popleft())  # 输出：'y'，从左侧弹出

  # 查看当前deque的内容
  print(list(d))  # 输出：['x', 'a', 'b']

  # 创建一个有长度限制的deque
  limited_d = deque(maxlen=3)
  limited_d.append('a')
  limited_d.append('b')
  limited_d.append('c')
  limited_d.append('d')  # 'a' 被移除，因为超过了最大长度限制

  print(list(limited_d))  # 输出：['b', 'c', 'd']
  ```
* 区间元素个数
  * **[** 左闭右开区间 **)**：**[** 1, n **)** 个数为 **n-1 = n-1** 个元素
  * **[** 左闭右闭区间 **]**：**[** 1, n **]** 个数为 **n-1+1 = n** 个元素
  * **减法性质**：`1, 2, 3, 4, 5`, 其中 `5-3 = 2`，**意味着连 `3` 一起减掉**，剩下 `4, 5`；同时，也可以理解为 `5` 反向减掉了 `3` 个数，此时下标为 `2`
  * **`减法本质就是半开半闭的模型，其实是左开右闭的`**，例如，从n开始往后选择`k`个数，则数的集合为 {n, n-1, ..., n-k+1, **~~`n-k`~~**}；例如上侧问题，如果是`[n-k, n]`，则一共 `k+1` 个元素。即 `n-k` 剩下的数的区间是 **`(n-k, n]`**，即 `[n-k+1, n]`

* **下标从0开始的模型**
  * 可以(参见909. 蛇梯棋.py)，非常利于下标转换，例如
    ```python
    arr = 
      [
        [1,  2,  3,  4,  5,  6],
        [12, 11, 10, 9,  8,  7],
      ]
    # 计算任意的n对应的下标
    # 分析：2行 x 6列，因此 行 必然是需要 除 6
    # 1～6:为第一行；7～12为第二行
    row = (n-1) // 6 # 如果下标不从0开始，1//6 = 0；6//6 = 1，行不一致；而直接减1，会使得下标从0开始，即行的下标也从0开始，和程序本身所求完美契合
    col = (n-1) % 6 if row % 2 == 1 else 6 - (n-1) % 6 - 1
    ```
  * 非常便于遍历编写 
    ```python
    # case 1
    for i in range(n): print(i) # 输出 0-n-1，正好遍历n次

    # case 2
    i=0
    while i<n: 
      print(i) # 同样遍历n次，从0-n-1
      i+=1 
    ```