'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
       start=-1
       max_len=0
       i=0
       if len(s)==0: return ''
       '''
       要么相隔一位相同，要么相隔两位相同，还可能二者都满足
       程序的逻辑控制，集合关系，统计几次的问题:

       易错点：
        相隔一位统计一次 且 相隔两位统计一次
        而非相隔一次或者两次只作一次统计

        总结：注意程序的总体架构
            或者的关系 if;if   或者 if c1 or c2
            且的关系if c1 and c1
            集合逐渐变小，即通过筛选，也就是嵌套if完成

        最后：
            能用python本身语言特性的，就用python本身特性，别去实现python已经封装的底层代码，这很原始
       '''
       while i<len(s):
            if i-1>=0 and s[i]==s[i-1]:
                p,q=i-1,i
                # print('one: ',p,q)
                while p>=0 and q<len(s) and s[p]==s[q]:
                    if q-p>max_len:
                            start=p
                            max_len=q-p
                            # print('---',p,max_len)
                    '''
                    #注意程序控制逻辑的化简
                    if s[p]==s[q]:
                        if q-p>max_len:
                            start=p
                            max_len=q-p
                            # print('---',p,max_len)
                    else:
                        break
                    '''
                    p-=1
                    q+=1
            if i-2>=0 and s[i]==s[i-2]:
                p,q=i-2,i
                # print('two: ',p,q)
                while p>=0 and q<len(s) and s[p]==s[q]: #如果嵌套循环里面只有一种if那么可以省略
                    if q-p>max_len:
                        start=p
                        max_len=q-p
                        # print('---',p,max_len)
                    p-=1
                    q+=1
            i+=1
       return s[start:start+max_len+1] if start>=0 else s[0]



       