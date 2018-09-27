class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # def find_val(nums, val):

        idx1 = 0
        res = 0
        while idx1 != len(nums):
            while idx1 != len(nums) and nums[idx1] != val:
                idx1 += 1
            if idx1 == len(nums):
                return idx1
            res += 1
            idx2 = idx1 + 1
            while idx2 != len(nums) and nums[idx2] == val:
                idx2 += 1
            if idx2 == len(nums):
                return idx1
            nums[idx1], nums[idx2] = nums[idx2], nums[idx1]
            idx1 += 1
        return idx1


nums = [2]
s = Solution()

print(s.removeElement(nums, 3))
