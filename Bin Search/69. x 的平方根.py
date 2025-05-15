"""
[easy]

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

 

示例 1：

输入：x = 4
输出：2
示例 2：

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
 

提示：

0 <= x <= 231 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if not x: return 0
        left, right = 1, x // 2
        while left < right:
            mid = left + (right - left) // 2
            lower_edge, upper_edge = mid ** 2, (mid + 1) ** 2
            if lower_edge <= x < upper_edge:
                return mid
            elif x < lower_edge:
                right = mid
            else:
                left = mid + 1
        return left

    # 二分法
    # 1. 设定初始值 l = 0, r = x
    # 2. 迭代公式 mid = (l + r) // 2
    # 3. 判断 mid * mid 是否小于等于 x
    # 4. 如果小于等于 x，则更新 ans = mid, l = mid + 1
    # 5. 否则更新 r = mid - 1
    # 6. 迭代直到 l > r
    # 7. 返回 ans
    # 8. 迭代次数不超过 100
    # 9. 迭代公式的收敛速度是 O(log n)
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    # 牛顿迭代法
    # 1. 设定初始值 x0 = x
    # 2. 迭代公式 x(i+1) = 0.5 * (xi + C / xi)
    # 3. 迭代直到收敛
    # 4. 收敛条件 abs(xi - x(i+1)) < 1e-7
    # 5. 返回整数部分
    # 6. 迭代次数不超过 100
    # 7. 迭代公式的收敛速度是 O(log n)
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        
        C, x0 = float(x), float(x)
        while True:
            # 公式推导：y = x^2 - C, y' = 2x
            # 切线方程：y = y' * (x - x0) + y0
            # 切线方程：y = 2x0 * (x - x0) + x0^2 - C 
            # 切线方程与x轴的交点：x = x0 - (x0^2 - C) / (2x0)
            # 迭代公式：x(i+1) = x0 - (x0^2 - C) / (2x0)
            # 迭代公式：x(i+1) = 0.5 * (x0 + C / x0)
            xi = 0.5 * (x0 + C / x0) 
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi # 更新迭代值，注意直接使用的是 xi，迭代速度更快
        
        return int(x0)

    # 二分法 左闭右开区间
    # ✅：1024 => 32*32
    # ❌：1023 => 31*31
    def mySqrt(self, x: int) -> int:
        e = 1e-2
        l, r = 0, x+1
        cnt = 0
        while l<r:
            m = l + (r-l)/2
            if abs(m**2-x) <= e:
                # print(l, r, x, m)
                return int(m)
            elif x < m**2:
                r = m
            else:
                l = m
            if cnt < 10:
                cnt += 1
        # print(l, r, m)
        return int(m)