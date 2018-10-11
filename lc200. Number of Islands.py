import queue


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        length = len(grid)
        length0 = len(grid[0])

        q = queue.Queue()
        visited = [[0] * length0 for i in range(length)]

        for i in range(length):
            for j in range(length0):
                if not visited[i][j] and grid[i][j] == '1':
                    q.put((i, j))
                    res += 1
                    while not q.empty():

                        isl = q.get()
                        if isl[0] < 0 or isl[0] >= length:
                            continue
                        if isl[1] < 0 or isl[1] >= length0:
                            continue
                        if not visited[isl[0]][isl[1]] and grid[isl[0]][isl[1]] == '1':
                            visited[isl[0]][isl[1]] = 1
                            q.put((isl[0] - 1, isl[1]))
                            q.put((isl[0] + 1, isl[1]))
                            q.put((isl[0], isl[1] - 1))
                            q.put((isl[0], isl[1] + 1))
        return res


snum = '''11000
11000
00100
00011'''
slst = snum.split('\n')
grid = [[int(x) for x in list(s)] for s in slst]
soln = Solution()
print(soln.numIslands(slst))
