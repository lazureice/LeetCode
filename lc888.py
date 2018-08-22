class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        sumA=sum(A)
        sumB=sum(B)
        dif=sumA-sumB
        tem=int(dif/2)
        A=set(A)
        B=set(B)
        for a in A:
        	if a-tem in B:
        		return [a,a-tem]

A = [1,2]
B = [2,3]

s=Solution()
res=s.fairCandySwap(A,B)

print(res)