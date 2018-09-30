class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        res = 1
        tem = ma = A[0]
        for i, x in enumerate(A):
            if x < ma:
                res = i + 1
                ma = tem
            else:
                if tem < x:
                    tem = x
        return res


A = [24, 11, 49, 80, 63, 8, 61, 22, 73, 85]
s = Solution()
print(s.partitionDisjoint(A))
