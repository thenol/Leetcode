'''
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/excel-sheet-column-title
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def convertToTitle(self, n: int) -> str:
        dic='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans=[]
        N=26
        while n:
            ans.append(dic[(n-1)%N])
            n=(n-1)//N
        return ''.join(ans)[::-1]