class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = j = 0
        length1, length2 = len(name), len(typed)
        while i < length1 and j < length2:
            while j < length2:
                if name[i] == typed[j]:
                    i, j = i + 1, j + 1
                    break
                else:
                    j += 1
        return i == length1


name = "laidden"
typed = "laiden"
s = Solution()
print(s.isLongPressedName(name, typed))
