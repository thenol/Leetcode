'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans=[]
        def dfs(s,path,level):
            nonlocal ans
            if s and level==1:
                if int(s)<=255: # check the last piece
                    if len(s)>=2 and s[0]=='0':
                        return 
                    ans.append('.'.join(path+[s]))
            else:
                for i in range(1,min(4,len(s))): 
                    if int(s[:i])<=255: # check before selecting the piece
                        if len(s[:i])>=2 and s[0]=='0':
                            continue
                        else:
                            dfs(s[i:],path[:]+[s[:i]],level-1)

        dfs(s,[],4)
        return ans