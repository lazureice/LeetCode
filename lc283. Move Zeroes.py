class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        idx1 = 0
        while idx1 != len(nums):
            while nums[idx1] != 0 and idx1 != len(nums) - 1:
                idx1 += 1
            idx2 = idx1 + 1
            while idx2 != len(nums) and nums[idx2] == 0:
                idx2 += 1
            if idx2 == len(nums):
                return
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]


nums = [0, 1, 0, 3, 12]
s = Solution()

print(s.moveZeroes(nums))
