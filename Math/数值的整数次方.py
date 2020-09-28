'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

保证base和exponent不同时为0
'''

# 快速求幂

# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base==0:
            return 0
        if exponent==0:
            return 1
        e=abs(exponent)
        ans=1
        tmp=base
        while e>0:
            if e&1==1:
                ans*=tmp
            e>>=1
            tmp*=tmp
        return ans if exponent>0 else 1/ans