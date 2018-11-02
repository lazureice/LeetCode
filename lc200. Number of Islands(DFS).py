class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(i, j):
            if i < 0 or i >= length:
                return
            if j < 0 or j >= length0:
                return
            if not visited[i][j] and grid[i][j] == '1':
                visited[i][j] = 1
                bfs(i - 1, j)
                bfs(i + 1, j)
                bfs(i, j - 1)
                bfs(i, j + 1)
        if not grid:
            return 0
        res = 0
        length = len(grid)
        length0 = len(grid[0])
        visited = [[0] * length0 for i in range(length)]

        for i in range(length):
            for j in range(length0):
                if not visited[i][j] and grid[i][j] == '1':
                    bfs(i, j)
                    res += 1
        return res


snum = '''11000
11000
00100
00011'''
slst = snum.split('\n')
grid = [[int(x) for x in list(s)] for s in slst]
soln = Solution()
print(soln.numIslands(slst))
