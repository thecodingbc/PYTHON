'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

'''
Analysis:
Because the parentheses / square brackets / curely brackets have to be perfectly matched.
I can use a stack to mimic the matching relationship.

When I see a ( [ {, I will push it to the stack.
When I see a ) ] }, I will pop a character out of the stack, and check whether the popped out character matched with the current character

if it doesn't match, then return False
if it matches, then I continue to process the next character
'''


class Solution:
    def isValid(self, s: str) -> bool:

        l = []

        for ch in s:

            if ch == '(' or ch == '[' or ch == '{':
                l.append(ch)

            elif ch == ')' and len(l) > 0 and l[-1] == '(':
                l.pop()

            elif ch == ']' and len(l) > 0 and l[-1] == '[':
                l.pop()

            elif ch == '}' and len(l) > 0 and l[-1] == '{':
                l.pop()

            else:
                return False

        if len(l) > 0:
            return False

        return True