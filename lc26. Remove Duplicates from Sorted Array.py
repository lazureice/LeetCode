class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] != nums[idx]:
                idx += 1
                nums[idx] = nums[i]

        return idx + 1


nums = [1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
