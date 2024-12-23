'''
[medium]

字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

 

示例 1:

输入: 
first = "pale"
second = "ple"
输出: True
 

示例 2:

输入: 
first = "pales"
second = "pal"
输出: False

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/one-away-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        def check(first,second):
            for i in range(len(first)):
                if second==first[:i]+first[i+1:]:return True
            return False 
        if first==second:return True # zero time
        if abs(len(first)-len(second))>=2:# two or more times
            return False
        if len(first)==len(second):# one times => replace
            count=0
            for i in range(len(first)):
                if first[i]!=second[i]:
                    count+=1
            if count>1:return False
            return True
        else: # delete
            if len(first)>len(second):
                return check(first,second)
            else:
                return check(second,first)
        