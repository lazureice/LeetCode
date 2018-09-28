class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        ress = []
        for x in nums:
            if x == 1:
                res += 1
            else:
                ress.append(res)
                res = 0
        ress.append(res)
        return max(ress)


nums = [1, 1, 0, 1, 1, 1]
s = Solution()
print(s.findMaxConsecutiveOnes(nums))
