class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s2 = list(S)
        i = 0
        j = len(S) - 1
        while i < j:
            if S[i].isalpha():
                if S[j].isalpha():
                    s2[i], s2[j] = s2[j], s2[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            else:
                i += 1
        return ''.join(s2)
