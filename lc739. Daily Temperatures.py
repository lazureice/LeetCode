class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(T)
        for i in range(len(T)):
            while len(stack) != 0 and T[i] > T[stack[-1]]:
                tem = stack.pop()
                res[tem] = i - tem
            stack.append(i)
        return res
