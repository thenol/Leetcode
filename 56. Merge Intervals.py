'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''



# color
# Unable to deal with adjacent areas
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start=0
        end=0
        for it in intervals:
            start=start if start<it[0] else it[0]
            end=end if end>it[1] else it[1]
        bias=0-start if start<0 else 0
        color=[0]*(end-start+1) # including the final number
        for it in intervals:
            for i in range(it[0]+bias,it[1]+1+bias):
                color[i]=1
            # print(it[0],it[1],color,len(color))
        res=[]
        left=-1
        for k,v in enumerate(color):
            if v==1 and left<0:
                left=k
            elif v==0 and left>=0:
                res.append([left-bias,k-bias-1])
                left=-1
            elif k==len(color)-1 and left>=0: # the end
                res.append([left-bias,k-bias])
            
            
        return res
'''


# method 2:
# merge area by a group of two
'''
def merge_two(arr):
    a1=arr[0]
    a2=arr[1]
    print(a1,a2)
    if a1[0]<=a2[0]:
        left=a1[0]
        if a1[1]>a2[0]:
            return [left,max(a1[1],a2[1])]
        else:
            return [a1,a2]
    else:
        left=a2[0]
        if a2[1]>a1[0]:
            return [left,max(a2[1],a1[1])]
        else:
            return [a2,a1]
'''


# sort the array
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if not intervals:
            return []
        ans=[intervals[0]]
        # print(intervals)
        for v in intervals:
            if ans[-1][1]>=v[0]:
                ans[-1]=[min(ans[-1][0],v[0]),max(ans[-1][1],v[1])]
            else:
                ans.append(v)
        return ans