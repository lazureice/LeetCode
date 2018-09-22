class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        res = []
        direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        pos = [0, 0]
        N = len(matrix)
        M = len(matrix[0])
        left, right = -1, M
        top, button = -1, N
        size = M * N
        for i in range(size):
            # print(pos[0], pos[1])
            res.append(matrix[pos[0]][pos[1]])
            if pos[1] + direcs[d][1] == right:
                d = (d + 1) % 4
                top += 1
            elif pos[1] + direcs[d][1] == left:
                d = (d + 1) % 4
                button -= 1
            elif pos[0] + direcs[d][0] == button:
                d = (d + 1) % 4
                right -= 1
            elif pos[0] + direcs[d][0] == top:
                d = (d + 1) % 4
                left += 1

            pos[0] += direcs[d][0]
            pos[1] += direcs[d][1]
        return res


nums = [
]
s = Solution()
print(s.spiralOrder(nums))
