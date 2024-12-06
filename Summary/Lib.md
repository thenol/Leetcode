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
  * **减法性质**：`1, 2, 3, 4, 5`, 其中 `5-3 = 2`，意味着连 `3` 一起减掉，剩下 `4, 5`；同时，也可以理解为 `5` 反向减掉了 `3` 个数，此时下标为 `2`
  * **`减法本质就是半开半闭的模型，其实是左开右闭的`**，例如，从n开始往后选择`k`个数，则数的集合为 {n, n-1, ..., n-k+1, **~~`n-k`~~**}；例如上侧问题，如果是`[n-k, n]`，则一共 `k+1` 个元素。即 `n-k` 剩下的数的区间是 **`(n-k, n]`**，即 `[n-k+1, n]`