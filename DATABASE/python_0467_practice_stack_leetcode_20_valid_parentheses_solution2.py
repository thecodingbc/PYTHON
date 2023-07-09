
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:

        l = deque()

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



'''
deque means: Double Ended QUEue
'''

'''
list

ArrayList - _ _ _ _ _ _ _ very fast in random access 
LinkList  - very slow in random access, very fast in insert & delete 


class LinkListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''