class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        operators = {'+', '-', '*', '/'}
        oprd = []
        # use lambda expression
        ops = {
            '*': lambda x, y: x * y,
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            # int() trunc to 0
            '/': lambda x, y: int(x / y),
        }

        for tk in tokens:
            if tk in operators:
                b = oprd.pop()
                # no need to pop another operand
                oprd[-1] = ops[tk](oprd[-1], b)
            else:
                oprd.append(int(tk))
        return oprd[0]


tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
s = Solution()
print(s.evalRPN(tokens))
