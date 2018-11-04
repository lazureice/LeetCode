from bisect import bisect_left


class RecentCounter:

    def __init__(self):
        self.lst = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.lst.append(t)
        lo = bisect_left(self.lst, (t - 3000))
        return len(self.lst) - lo


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
for t in [1, 100, 3001, 3002]:
    param_1 = obj.ping(t)
    print(param_1)
