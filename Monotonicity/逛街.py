'''
[qq]

时间限制：C/C++ 2秒，其他语言4秒

空间限制：C/C++ 256M，其他语言512M

小Q在周末的时候和他的小伙伴来到大城市逛街，一条步行街上有很多高楼，共有n座高楼排成一行。
小Q从第一栋一直走到了最后一栋，小Q从来都没有见到这么多的楼，所以他想知道他在每栋楼的位置处能看到多少栋楼呢？（当前面的楼的高度大于等于后面的楼时，后面的楼将被挡住） 

输入描述:
输入第一行将包含一个数字n，代表楼的栋数，接下来的一行将包含n个数字wi(1<=i<=n)，代表每一栋楼的高度。
1<=n<=100000;
1<=wi<=100000; 

输出描述:
输出一行，包含空格分割的n个数字vi，分别代表小Q在第i栋楼时能看到的楼的数量。

输入例子1:
6
5 3 8 3 2 5

输出例子1:
3 3 5 4 4 4

例子说明1:
当小Q处于位置3时，他可以向前看到位置2,1处的楼，向后看到位置4,6处的楼，加上第3栋楼，共可看到5栋楼。当小Q处于位置4时，他可以向前看到位置3处的楼，向后看到位置5,6处的楼，加上第4栋楼，共可看到4栋楼。
'''


# brutal: 40% 
from collections import deque

n=int(input().strip())
nums=list(map(int,input().strip().split(' ')))
lq=deque([])
ans=[]
for i in range(len(nums)):
    rq=deque([])
    while lq and nums[lq[-1]]<nums[i-1]:
        lq.pop()
    if i>0:
        lq.append(i-1)
    for j in range(i+1,len(nums)):
        if not rq:
            rq.append(j)
            continue
        while rq and nums[rq[-1]]<nums[j]:
            rq.append(j)
    ans.append(len(lq)+len(rq)+1)
    #print([nums[_] for _ in lq],[nums[_] for _ in rq])
for i in ans:
    print(i,end=' ')
    


# monotonic
def buildings(n, nums):
    lstack, rstack = [nums[0]], [nums[n-1]]
    lrst, rrst =[1], [1]
    for i in range(1,n):
        lrst.append(len(lstack)+1)
        rrst.append(len(rstack)+1)
        while len(lstack)!=0 and nums[i]>=lstack[-1]:lstack.pop()
        while len(rstack)!=0 and nums[n-1-i]>=rstack[-1]:rstack.pop()
        lstack.append(nums[i])
        rstack.append(nums[n-1-i])
    rrst = [r for r in reversed(rrst)]
    res =[lrst[i] + rrst[i] -1 for i in range(n)]
    return res
 
if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split(' ')))
    res = buildings(n, nums)
    print(" ".join(list(map(str, res))))