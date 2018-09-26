class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 0
        for x in nums[::2]:
            res += x
        return res


nums = [1, 4, 3, 2]
s = Solution()
print(s.arrayPairSum(nums))
