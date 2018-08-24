from collections import Counter

# Counter 检查数量是否相等，返回一个字典对象（数据结构是散列表）
class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        count_N=Counter(str(N))
        # any: 只要有一个True，就返回True，全部为False，则返回False
        return any(count_N==Counter(str(1<<i)) for i in range(31))
            
            
s=Solution()

print(s.reorderedPowerOf2(635824465))
