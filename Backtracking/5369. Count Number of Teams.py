'''
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if:  (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

 

Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1). 
Example 2:

Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.
Example 3:

Input: rating = [1,2,3,4]
Output: 4
 

Constraints:

n == rating.length
1 <= n <= 200
1 <= rating[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-teams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        ans=[]
        def dfs(num,path,level,asc): #  
            if level==0:
                # print(path,num,asc)
                ans.append(path)
            else:
                for i in range(len(num)):
                    if asc and path and num[i]>path[-1]:
                        dfs(num[i+1:],path[:]+[num[i]],level-1,asc)
                    elif not asc and path and num[i]<path[-1]:
                        dfs(num[i+1:],path[:]+[num[i]],level-1,asc)
                    elif not path:
                        dfs(num[i+1:],path[:]+[num[i]],level-1,asc)
        if not rating:
            return 0
        for i in range(len(rating)):
            dfs(rating[i+1:],[rating[i]],2,True)
            dfs(rating[i+1:],[rating[i]],2,False)
        return len(ans)
                