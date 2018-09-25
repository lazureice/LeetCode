class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


haystack = "hello"
needle = ""

s = Solution()

print(s.strStr(haystack, needle))
