class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # if not rowIndex:
        #     return [1]
        res = [1]
        for i in range(1, rowIndex + 1):
            tem = []
            tem.append(1)
            for j in range(1, i):
                x = res[j] + res[j - 1]
                tem.append(x)
            tem.append(1)
            res = tem
        return res


num = 1
s = Solution()
print(s.getRow(num))
