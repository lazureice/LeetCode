class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def helper(heights):
            cur = 0
            ret = 0
            for h in heights:
                ret += abs(h - cur)
                cur = h
            ret += abs(cur)
            return ret

        area = 0
        for row in grid:
            area += helper(row)

        for col in zip(*grid):
            area += helper(col)

        area += sum(2 for row in grid for h in row if h > 0)
        return area
