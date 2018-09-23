class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = max(A) - min(A) - 2*K
        return res if res > 0 else 0


A = [1,3,6]
K = 3
s = Solution()
print(s.smallestRangeI(A, K))
