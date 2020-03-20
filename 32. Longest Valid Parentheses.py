class Solution:
    def longestValidParentheses(self, s: str) -> int:
        s=count=mx=0
        for c in s:
            if c=='(':
                count+=1
                s+=1
                mx+=1
            elif c==')':
                s-=1
                if s==0:
                    if count>mx:
                        mx=count
                    
                count=0
        return mx