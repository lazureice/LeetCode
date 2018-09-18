class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxnum = nums[0]
        secmax = 0
        result = True
        idx = 0
        for i in range(1, len(nums)):
            if nums[i] > maxnum:
                idx = i
                secmax = maxnum
                maxnum = nums[i]
                result = (maxnum >= 2 * secmax)
            else:
                if maxnum < 2 * nums[i]:
                    result = False
        return idx if result else -1


nums = [1, 2, 3, 4]
s = Solution()
print(s.dominantIndex(nums))
