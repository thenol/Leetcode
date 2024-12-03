# 常用函数

* 查找
  * 二分查找
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