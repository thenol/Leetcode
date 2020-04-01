


# //考虑所有长度的子串
# for (int len = 1; len <= length; len++) {
#     //从每个下标开始
#     for (int i = 0; i <= s.length() - len; i++) {
#         int j = i + len - 1;
#         dp[i][j] = s.charAt(i) == s.charAt(j) && (len < 3 || dp[i + 1][j - 1]);
#     }
# }

