class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=''
        last=-1
        while last>=-len(s) and s[last]==' ':last-=1
        if last==-len(s)-1:
            return 0
        elif last<-1:
            s=s[-len(s):last+1]  # the slice !!!!!!!
        for i in range(-1,-len(s)-1,-1):
            if not s[i]==' ':
                c+=s[i]
            else:
                break
        return len(c[::-1])