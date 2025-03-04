"""
时间复杂度：O(n)
思路：在埃氏筛法的基础上，让每个合数只被它的 “最小质因子” 筛选一次，以达到不重复的目的。
"""
pri = []
not_prime = [False] * N # 初始全部设置为素数


def pre(n):
    for i in range(2, n + 1):
        if not not_prime[i]:
            pri.append(i)
        for pri_j in pri:
            if i * pri_j > n: # 超过筛选范围n，直接跳出
                break 
            not_prime[i * pri_j] = True # 标记合数
            if i % pri_j == 0:
                """
                i % pri_j == 0
                换言之，i 之前被 pri_j 筛过了
                由于 pri 里面质数是从小到大的，所以 i 乘上其他的质数的结果一定会被
                pri_j 的倍数筛掉，就不需要在这里先筛一次，所以这里直接 break
                掉就好了
                """
                break

# 理解最后一个break
"""
      pri: 2, 3
        i: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
not_prime: F, F, T, T, T, F, F, F,  F,  F,  F

解释：
    当i=4时，pri_j 遍历 pri 中的素数，注意为了让每个合数只被自己最小质因子标记一次，
    此时，pri_j=2, 标注 2*4=8 为合数，但是此时 4%2=0，说明 4 一定有质因子 2 ，
    且由于pri从头开始遍历，因此 2 一定是最小质因子。

    而此时无需再继续遍历后续的素数 3，然后来标记 3*4=12，因为 12 一定还会被最小质因子标记，
    原因很简单，因为不管pri中后续的质数是什么，假如为 k，则 k*4 % 2=0 恒成立，一定会当 i=(k*4)/2 的时候再次被2标记
    如上 3*4/2 = 6，也就是当i=6 的时候会被再次标记，因此就重复了，就会导致和埃筛法一样，所以直接break掉就行了
    
    相当于将 i 的后续倍数继续交由 pri_j来筛就行了，不用 i 自己和后面素数再筛一遍

"""


def prime(self, n: int) -> int:
    # 素数筛
    p = []
    is_p = [True]*(n+1)
    for i in range(2, n):
        if is_p[i]:
            p.append(i)
        for j in p:
            if j*i > n:
                break
            is_p[j*i] = False

            if i%j == 0: # 被前面的筛过了，不用再筛了，也就是能被4筛的，一定都被2筛过了
                break