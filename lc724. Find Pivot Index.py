class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1

        lsum = nums[0]
        rsum = sum(nums)
        if lsum == rsum:
            return 0
        for i in range(1, n):
            lsum += nums[i]
            rsum -= nums[i - 1]
            if lsum == rsum:
                return i
        else:
            return -1


# test
nums = [-1, -1, -1, 0, 1, 1]
s = Solution()
print(s.pivotIndex(nums))
