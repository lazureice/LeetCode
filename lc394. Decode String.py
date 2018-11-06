class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for c in s:

            if c != ']':
                stack.append(c)
            else:
                tem = ''
                ch = stack.pop()

                while ch.isalpha():
                    tem = ch + tem
                    ch = stack.pop()
                if stack[-1].isnumeric():
                    num = int(stack.pop())
                else:
                    num = 1
                stack.append(tem * num)

        return ''.join(stack)


sol = Solution()
s = "3[a2[c]]"
print(sol.decodeString(s))
