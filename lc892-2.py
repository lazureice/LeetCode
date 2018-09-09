class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # 外面，包括凹下去的。
        # 欣宜还是考虑复杂了，负的也没关系，用绝对值就行了。不需要两个方向都跑一次。
        def helper(heights):
            cur = 0
            ret = 0
            for h in heights:
                ret += abs(h - cur)
                cur = h
            ret += abs(cur)
            return ret

        area = 0
        # 每一行
        for row in grid:
            area += helper(row)

        # 每一列
        for col in zip(*grid):
            area += helper(col)

        # 上下底面
        area += sum(2 for row in grid for h in row if h > 0)
        return area
