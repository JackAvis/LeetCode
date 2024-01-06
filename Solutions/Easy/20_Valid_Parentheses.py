class Solution(object):
    def isValid(self, s):
        stack = []
        m = {'(': ')',
            '{': '}',
            '[': ']'}
        check = [']', '}', ')']
        for char in s:
            if char in m:
                stack.append(m[char])
            if char in check:
                if len(stack) == 0:
                    return False
                if char != stack.pop():
                    return False
        return len(stack) == 0
            