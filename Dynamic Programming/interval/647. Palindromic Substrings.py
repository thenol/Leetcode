'''
[medium]
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindromic-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        N=len(s)
        f=[[False for _ in range(N)] for _ in range(N)]
        ans=0
        for i in range(N):
            f[i][i]=True
            ans+=1
        for le in range(2,N+1):#[]
            for i in range(len(s)-le+1):
                j=i+le-1 #i+le<len(s)=>i<len(s)-le
                if le==2 and s[i]==s[j]:
                    f[i][j]=True
                    ans+=1
                    continue
                if s[i]==s[j]:
                    f[i][j]=f[i+1][j-1]
                    if f[i][j]:ans+=1
                else:
                    f[i][j]=False
        return ans


