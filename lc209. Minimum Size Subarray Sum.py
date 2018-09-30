class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def bin_search(left, right, key, sums):
            while left <= right:
                mid = (left + right) // 2
                if sums[mid] >= key:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        length = len(nums)
        sums = [None] * (length + 1)
        sums[0] = 0

        for i in range(0, length):
            sums[i + 1] = sums[i] + nums[i]

        # 两层循环 O(N^2)解法
        # for i in range(1, length + 1):
        #     for j in range(length + 1 - i):
        #         if sums[j + i] - sums[j] >= s:
        #             return i

        res = length + 1
        for i in range(length + 1):
            # sums[right]-sums[left]，不包括nums[left]
            tem = bin_search(i + 1, length, sums[i] + s, sums)
            if tem == length + 1:
                break
            if tem - i < res:
                res = tem - i

        return 0 if res == length + 1 else res

s=100
nums=[]
soln = Solution()
print(soln.minSubArrayLen(s, nums))
