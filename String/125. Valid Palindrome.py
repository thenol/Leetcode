'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        check=lambda x: x.lower()>='a' and x.lower()<='z' or x>='0' and x<='9'
        while l<r:
            while l<r and not check(s[l]):l+=1
            while r>l and not check(s[r]):r-=1
            if not l==r and not s[l].lower()==s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True