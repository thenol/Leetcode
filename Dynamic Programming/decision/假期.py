'''
链接：https://www.nowcoder.com/questionTerminal/7cd9a140387e455a972e8fea0e74be2c
来源：牛客网

由于业绩优秀，公司给小Q放了 n 天的假，身为工作狂的小Q打算在在假期中工作、锻炼或者休息。他有个奇怪的习惯：不会连续两天工作或锻炼。只有当公司营业时，小Q才能去工作，只有当健身房营业时，小Q才能去健身，小Q一天只能干一件事。给出假期中公司，健身房的营业情况，求小Q最少需要休息几天。

输入描述:
第一行一个整数 n(1\leq n\leq 100000)n(1≤n≤100000) 表示放假天数
第二行 n 个数 每个数为0或1,第 i 个数表示公司在第 i 天是否营业
第三行 n 个数 每个数为0或1,第 i 个数表示健身房在第 i 天是否营业
（1为营业 0为不营业）


输出描述:
一个整数，表示小Q休息的最少天数
示例1
输入
4
1 1 0 0
0 1 1 0
输出
2
说明
小Q可以在第一天工作，第二天或第三天健身，小Q最少休息2天
'''
# https://www.nowcoder.com/test/question/done?tid=36389337&qid=830863#summary
day=int(input())
_C=input()
c=[int(i) for i in _C.split()]
_G=input()
g=[int(i) for i in _G.split()]
 
a=[c.copy(),g.copy()]

#a[:][i]表示到第i天为止已经工作或运动的天数。
for i in range(day-1):
    if c[i]==0:
        a[0][i+1]+=a[0][i] if a[0][i] > a[1][i] else a[1][i]
    else:
        a[0][i+1]+=a[1][i]
    if g[i]==0:
        a[1][i+1]+=a[0][i] if a[0][i] > a[1][i] else a[1][i]
    else:
        a[1][i+1]+=a[0][i]
 
print(day-(a[0][day-1] if a[0][day-1]>a[1][day-1] else a[1][day-1]))