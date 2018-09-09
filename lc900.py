# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)


class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.index = -1
        self.A = []
        for i in range(len(A))[::2]:
            self.A += [A[i + 1]] * A[i]

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.index += n
        if self.index > len(self.A) - 1:
            return - 1
        return self.A[self.index]


A = [3, 8, 0, 9, 2, 5]
s = RLEIterator(A)
print(s.next(2))
print(s.next(1))
print(s.next(1))
print(s.next(2))