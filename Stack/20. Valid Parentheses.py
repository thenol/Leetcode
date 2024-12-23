'''
[easy]

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# version 1: stack + 3 states
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dic={')':'(','}':'{',']':'['}
        for c in s:
            if c=='(' or c=='{' or c=='[':
                stack.append(c)
            else:
                if stack and stack[-1]!=dic[c]:
                    return False
                else:
                    if stack:
                        stack.pop(-1)
                    else:
                        return False
        if stack:return False
        return True

# version 2: stack + 4 states

class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','[':']','{':'}',-1:''}
        stack=[]
        for v in s:
            if v in dic:
                stack.append(v)
            else:
                top=stack.pop() if stack else -1
                if dic[top]==v:
                    continue
                else:
                    return False
        if stack:
            return False
        return True