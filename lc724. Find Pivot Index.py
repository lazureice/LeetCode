class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsum = 0
        rsum = sum(nums)
        for i, num in enumerate(nums):
            lsum += num
            if lsum == rsum:
                return i
            rsum -= num
        else:
            return -1


# test
nums = [1, 7, 3, 6, 5, 6]
s = Solution()
print(s.pivotIndex(nums))
