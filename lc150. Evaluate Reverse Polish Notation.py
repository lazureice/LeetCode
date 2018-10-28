class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-', '*', '/'}
        oprd = []

        for tk in tokens:
            if tk in operators:
                b = oprd.pop()
                a = oprd.pop()
                if tk == '+':
                    c = a + b
                elif tk == '-':
                    c = a - b
                elif tk == '*':
                    c = a * b
                else:
                    c = int(a / b)
                oprd.append(c)
            else:
                oprd.append(int(tk))
        return oprd[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(tokens))
