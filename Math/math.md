# 数学相关函数实现
## 最大公约数 `math.gcd`
> ❗️注意：math.gcd和math.lcm都可以传入多个数作为参数，参数为 `*nums`
> math.prod 计算连乘，参数为`list` 
math.gcd() 函数在 Python 的标准库 math 中，用于计算两个整数的最大公约数（GCD）。这个函数的实现基于欧几里得算法，这是一种非常高效的计算最大公约数的方法。

欧几里得算法
欧几里得算法的基本思想是：两个整数 a 和 b（假设 a > b）的最大公约数等于 b 和 a % b 的最大公约数。这个过程可以一直重复，直到 b 变为 0，此时的 a 就是最大公约数。
```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)
# a = m*d; b = c*d

```