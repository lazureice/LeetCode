class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif d[stack.pop()] != c:
                    return False
        return len(stack) == 0
