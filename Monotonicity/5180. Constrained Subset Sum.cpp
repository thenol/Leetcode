// Given an integer array nums and an integer k, return the maximum sum of a non-empty subset of that array such that for every two consecutive integers in the subset, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

// A subset of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.

//  

// Example 1:

// Input: nums = [10,2,-10,5,20], k = 2
// Output: 37
// Explanation: The subset is [10, 2, 5, 20].
// Example 2:

// Input: nums = [-1,-2,-3], k = 1
// Output: -1
// Explanation: The subset must be non-empty, so we choose the largest number.
// Example 3:

// Input: nums = [10,-2,-10,-5,20], k = 2
// Output: 23
// Explanation: The subset is [10, -2, -5, 20].
//  

// Constraints:

// 1 <= k <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/constrained-subset-sum
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
# include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    int constrainedSubsetSum(vector<int>& nums, int k) {
        deque<int> q;
        int N=nums.size();
        int dp[N];
        for(int i=0;i<N;i++)dp[i]=nums[i];
        // bool find=false;
        int mx=-100000;
        q.push_back(0);
        mx=max(dp[0],mx);
        for(int i=1;i<N;i++){
            
            // optimize the dp using monotonic queue
            dp[i]=max(dp[i],dp[q.front()]+nums[i]);
            while(!q.empty()&&dp[q.back()]<dp[i])q.pop_back();
            q.push_back(i);
            if(i-q.front()==k)q.pop_front();
            
            // original stupid method
            // for(int j=1;j<=k&&i-j>=0;j++){
            //     dp[i]=max(dp[i],dp[i-j]+nums[i]);
            //     // if(!find && t!=dp[i+j])find=true;
            // }


            mx=max(mx,dp[i]);
        }
        for(int i=0;i<N;i++){
            cout<<dp[i]<<' ';
        }
        return mx;

    }
};