'''
[qq]

时间限制：C/C++ 2秒，其他语言4秒

空间限制：C/C++ 256M，其他语言512M

作为程序员的小Q，他的数列和其他人的不太一样，他有个数。
老板问了小Q一共 m次，每次给出一个整数, 要求小Q把这些数每分为一组，然后把每组进行翻转，小Q想知道每次操作后整个序列中的逆序对个数是多少呢？

例如:
对于序列1 3 4 2，逆序对有(4, 2),(3, 2),总数量为2。
翻转之后为2 4 3 1，逆序对有(2, 1),(4, 3), (4, 1), (3, 1),总数量为4。

输入描述:
第一行一个数
第二行个数，表示初始的序列()
第三行一个数
第四行m个数表示

输出描述:
m行每行一个数表示答案。

输入例子1:
2
2 1 4 3
4
1 2 0 2

输出例子1:
0
6
6
0

例子说明1:
初始序列2 1 4 3
2^{q_1} = 2 ->
第一次：1 2 3 4 -> 逆序对数为0
2^{q_2} = 4 ->
第二次：4 3 2 1 -> 逆序对数为6
2^{q_3} = 1 ->
第三次：4 3 2 1 -> 逆序对数为6
2^{q_4} = 4 ->
第四次：1 2 3 4 -> 逆序对数为0
'''


# brutal: 30%


n=int(input().strip())
nums=list(map(int,input().strip().split(' ')))
m=int(input().strip())
q=list(map(int,input().strip().split(' ')))

def rev(nums):
    count=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                count+=1
    return count

def inv(nums,g):
    ret=[]
    for i in range(len(nums)):
        if (i+1)%g==0:
            ret+=nums[i+1-g:i+1][::-1]
    return ret

for i in range(len(q)):
    res=inv(nums,2**q[i])
    ans=rev(res)
    nums=res
    #print(nums,res,ans)
    print(ans)



