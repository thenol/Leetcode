// Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

// Follow up:
// Could you solve it in linear time?

// Example:

// Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
// Output: [3,3,5,5,6,7] 
// Explanation: 

// Window position                Max
// ---------------               -----
// [1  3  -1] -3  5  3  6  7       3
//  1 [3  -1  -3] 5  3  6  7       3
//  1  3 [-1  -3  5] 3  6  7       5
//  1  3  -1 [-3  5  3] 6  7       5
//  1  3  -1  -3 [5  3  6] 7       6
//  1  3  -1  -3  5 [3  6  7]      7
//  

// Constraints:

// 1 <= nums.length <= 10^5
// -10^4 <= nums[i] <= 10^4
// 1 <= k <= nums.length

// 来源：力扣（LeetCode）
// 链接：https://leetcode-cn.com/problems/sliding-window-maximum
// 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#include<bits/stdc++.h>

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> q;
        vector<int> ans;
        for(int i=0;i<nums.size();i++){
            while(!q.empty()&&nums[q.back()]<nums[i])q.pop_back();
            q.push_back(i);
            if(i-q.front()==k)q.pop_front();
            if(i>=k-1)
                ans.push_back(nums[q.front()]);
        }
        return ans;
    }
};