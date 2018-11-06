class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        num = ''
        i = 0
        while i < len(s):

            if s[i].isnumeric():
                while s[i].isnumeric():
                    num += s[i]
                    i += 1

                stack.append(num)
                num = ''

            elif s[i] != ']':
                stack.append(s[i])
                i += 1
            else:
                tem = ''
                ch = stack.pop()

                while ch.isalpha():
                    tem = ch + tem
                    ch = stack.pop()
                if stack[-1].isnumeric():
                    n = int(stack.pop())
                else:
                    n = 1
                stack.append(tem * n)
                i += 1

        return ''.join(stack)


sol = Solution()
s = "100[leetcode]"
print(sol.decodeString(s))
