'''
Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] 
Example 2:

Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]
Example 3:

Input: num = "105", target = 5
Output: ["1*0+5","10-5"]
Example 4:

Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]
Example 5:

Input: num = "3456237490", target = 9191
Output: []
 

Constraints:

0 <= num.length <= 10
num only contain digits.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/expression-add-operators
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''