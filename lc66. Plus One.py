class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(s) for s in list(str(int(''.join([str(x) for x in digits])) + 1))]


digits = [4, 3, 2, 1]
s = Solution()
print(s.plusOne(digits))
