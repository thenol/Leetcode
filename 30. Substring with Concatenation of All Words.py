class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        '''
        法一:回溯法
        '''
        dic={}
        for i in words:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1

        is_word=False
        count=0
        if s=='' or len(words)==0: return []
        n=len(words[0])
        res=[]
        i=0
        while i+n <=len(s): #左闭右开
            if s[i:i+n] in dic:
                if not is_word: #初始匹配
                    is_word=True
                    t={k:v for k,v in dic.items()}
                    count=1
                else:
                    count+=1

                t[s[i:i+n]]-=1
                i+=n

                # print(s[i-n:i],count,t,i,i+n*len(words))
                if count==len(words):
                    not_sub=False
                    for k,v in t.items():
                        if v!=0:
                            not_sub=True
                            break
                    # print('-'*20,not_sub)
                    if not not_sub:
                        res.append(i-n*count)
                        # print('='*20)
                    i=i-n*(count)+1
                    # print('next i is ',i)
                    not_sub=False
                    is_word = False
                    count=0 #从下一个单词开始找
            else:
                is_word=False
                if count>0:
                    i=i-n*(count)+1
                else:
                    i+=1
                count=0
                
        return res
                


                    



  



