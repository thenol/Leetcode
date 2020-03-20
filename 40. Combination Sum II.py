class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #recursive

        
        candidates.sort() # Deduplication 1
        def rec(candidates,target):
            res=[]
            last=''
            for k,v in enumerate(candidates):
                if v==last: # Deduplication 2
                    continue
                else:
                    last=v
                if target-v==0:
                    # print(i)
                    res.append([v])
                elif target-v>0:
                    r=rec(candidates[k+1:],target-v)
                    for i in r:
                        res.append([v]+i)
                
            return res
        return rec(candidates,target)