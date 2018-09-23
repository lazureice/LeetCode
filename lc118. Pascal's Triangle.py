class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        # elif numRows == 1:
        #     return [[1]]
        # elif numRows == 2:
        #     return [[1], [1, 1]]

        # res = [[1], [1, 1]]
        res = [[1]]

        for i in range(1, numRows):
            tem = []
            tem.append(1)

            for j in range(1, i):

                x = res[i - 1][j] + res[i - 1][j - 1]
                tem.append(x)
            tem.append(1)
            res.append(tem)

        return res


num = 5
s = Solution()
print(s.generate(num))
