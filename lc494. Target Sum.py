from functools import lru_cache


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        @lru_cache(None)
        def dfs(su, i):
            if i == len(nums):
                return S == su
            res1 = dfs(su + nums[i], i + 1)
            res2 = dfs(su - nums[i], i + 1)
            return res1 + res2
        return dfs(0, 0)


nums = [10, 9, 6, 4, 19, 0, 41, 30, 27, 15,
        14, 39, 33, 7, 34, 17, 24, 46, 2, 46]
S = 45
s = Solution()
res = s.findTargetSumWays(nums, S)
print(res)
