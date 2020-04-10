'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        N=26
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        dic={alphabet[i]:i+1 for i in range(len(alphabet))}
        ans=0
        for i in range(len(s))[::-1]:
            ans+=N**(len(s)-i-1)*dic[s[i]]
        return ans