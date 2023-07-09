
from typing import List

class Solution(object):

    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token in ["+", "-", "*", "/"]:

                num2 = stack.pop()
                num1 = stack.pop()

                expression = num1 + token + num2

                stack.append(eval(expression))

            else:
                stack.append(token)

        return int(stack.pop())



