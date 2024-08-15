"""
时间复杂度 O(nloglogn)
思路：本质将数从小到大，标记自己的倍数，也就是合数（非质数），从而全部筛掉，剩下的就是质数
"""

n = 10**8  # 代求的范围中的最大值
k = 0
s = [True for i in range(n)]  # 首先默认所有数都是质数
z = []
for i in range(2,n):
    if s[i]:  # 判断是否为质数，如果没有被标记过，就是质数
        k+=1
        z.append(i) #添加质数
        for j in range(i+i,n,i):   # 每次找到一个质数后，就开始将是质数的倍数的数都改为False
            s[j] = False

print(k) # 个数
print(z) # 质数
