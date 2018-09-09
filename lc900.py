# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)


class RLEIterator:
    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.index = 0
        self.A = A
        self.len_a = len(A)

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(self.index, self.len_a, 2):
            mask = n - self.A[i]
            if mask > 0:
                n = mask
                self.index = i + 2
                continue
            elif mask < 0:
                self.A[i] -= n
                self.index = i
                return self.A[i + 1]
            else:
                self.index = i + 2
                return self.A[i + 1]
        else:
            return -1


A = [635, 606, 576, 391, 370, 981, 36, 21, 961, 185, 124, 210, 801, 937, 22, 426, 101, 260, 221, 647, 350, 180, 504, 39, 101,
     989, 199, 358, 732, 839, 919, 169, 673, 967, 58, 676, 846, 342, 250, 597, 442, 174, 472, 410, 569, 509, 311, 357, 838, 251]
s = RLEIterator(A)

B = [[5039], [62], [3640], [671], [67], [395], [262], [839], [74], [43], [42], [77], [13], [6], [3], [1], [1], [1], [1], [1], [1], [1], [
    1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1], [1]]
for b in B:
    print(s.next(b[0]),end=',')
