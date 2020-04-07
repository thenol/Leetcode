'''
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/repeated-dna-sequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dic={}
        N=len(s)
        n=10
        for i in range(N-n+1):
            if s[i:i+n] in dic:
                dic[s[i:i+n]]+=1
            else:
                dic[s[i:i+n]]=1
        
        ans=[]
        for k,v in dic.items():
            if v>=2:
                ans.append(k)
        return ans