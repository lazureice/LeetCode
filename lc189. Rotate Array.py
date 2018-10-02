class Solution:

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reserve(start, end):
            for i in range((end - start) // 2):
                nums[i + start], nums[end - i -
                                      1] = nums[end - i - 1], nums[i + start]

        length = len(nums)
        k %= length
        reserve(length - k, length)
        reserve(0, length - k)
        reserve(0, length)


nums = [1,2,3,4,5,6,7]
k = 3
s = Solution()
s.rotate(nums, k)
print(nums)
