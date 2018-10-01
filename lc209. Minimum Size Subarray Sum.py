class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        left = right = su = 0
        res = len(nums) + 1
        while right < len(nums):
            su += nums[right]
            right += 1
            if su >= s:
                while su >= s:
                    if right - left < res:
                        res = right - left
                    su -= nums[left]
                    left += 1
        return 0 if res == len(nums) + 1 else res


s = 7
nums = [2, 3, 1, 2, 4, 3]
soln = Solution()
print(soln.minSubArrayLen(s, nums))
