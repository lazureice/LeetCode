class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        direcs = [(-1, 1), (1, -1)]
        d = 0
        res = []
        pos = [0, 0]
        M = len(matrix)
        N = len(matrix[0])
        size = M * N
        for i in range(size):
            res.append(matrix[pos[0]][pos[1]])
            pos[0] += direcs[d][0]
            pos[1] += direcs[d][1]
            # 顺序不能变，先判断是否超过右边和下边。也就是==M or ==N，
            # 如果先判断是否==-1，那么在角上越界就会出错
            if pos[0] == M:
                pos[1] += 2
                d = 1 - d
                pos[0] = M - 1
            elif pos[1] == N:
                pos[1] = N - 1
                d = 1 - d
                pos[0] += 2
            elif pos[0] == -1:
                d = 1 - d
                pos[0] = 0
            elif pos[1] == -1:
                d = 1 - d
                pos[1] = 0

        return res


nums = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
s = Solution()
print(s.findDiagonalOrder(nums))
