


# //考虑所有长度的子串
# for (int len = 1; len <= length; len++) {
#     //从每个下标开始
#     for (int i = 0; i <= s.length() - len; i++) {
#         int j = i + len - 1;
#         dp[i][j] = s.charAt(i) == s.charAt(j) && (len < 3 || dp[i + 1][j - 1]);
#     }
# }

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        
        # comment:
        # The output of the sentence "map (str, nums)" is a list of strings as string objects.
        # Class LargerNumKey extends the String class, so it treats each string object in the list as a LargerNumKey object and then compares
        
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey)) 

        return '0' if largest_num[0] == '0' else largest_num

# Solution().largestNumber([2,1,3,5,6])
print(divmod(10,2))