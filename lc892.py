'''
之前有道题求投影，这个是求表面积，因此需要考虑凹的情况。
上下（也就是平行于xy平面）容易，依然是投影。

平行于yz、xz平面的分成两部分：
1. 先求周围一圈
2. 再求被挡住的
'''


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid[0])
        xy = sum(v > 0 for row in grid for v in row) * 2
        front = sum(x for x in grid[n - 1])
        back = sum(x for x in grid[0])
        left = sum(grid[i][0] for i in range(n))
        right = sum(grid[i][n - 1] for i in range(n))

        for i in range(n - 1):
            # front to back
            front += sum(max(grid[i][j] - grid[i + 1][j], 0) for j in range(n))
            # back to front
            back += sum(max(grid[i + 1][j] - grid[i][j], 0) for j in range(n))
            left += sum(max(grid[j][i + 1] - grid[j][i], 0) for j in range(n))
            right += sum(max(grid[j][i] - grid[j][i + 1], 0) for j in range(n))

        return xy + front + back + left + right


s = Solution()
grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
print(s.surfaceArea(grid))
