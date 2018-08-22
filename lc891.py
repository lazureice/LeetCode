'''不排序，把所有子数组找出来，然后把极差加起来，这是最麻烦的。
其次是排序之后二重循环
O(N)的是等比数列
'''

class Solution:
    def sumSubseqWidths(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        res=0
        n=len(A)

        for i in range(n):
            pos=(1<<i)
            neg=(1<<(n-1-i))
            res=(res+(pos-neg)*A[i])%(10**9+7)
        return res



A=[2,1,3]
s=Solution()
print(s.sumSubseqWidths(A))
