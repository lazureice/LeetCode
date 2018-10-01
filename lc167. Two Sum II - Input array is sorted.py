class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            tem = numbers[left] + numbers[right]
            if tem > target:
                right -= 1
            elif tem < target:
                left += 1
            else:
                return [left + 1, right + 1]


nums = [2, 7, 11, 15]
target = 9
s = Solution()
print(s.twoSum(nums, target))
