class Solution:
    def test(self, deck):
        dic = {}
        for x in deck:
            if dic.get(x) is None:
                dic[x] = 1

            else:
                dic[x] += 1
        for k, v in dic.items():
            print(k, v)

    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        dic = {}
        for x in deck:
            if dic.get(x) is None:
                dic[x] = 1

            else:
                dic[x] += 1

        min_num = min(x for x in dic.values())
        if min_num == 1:
            return False
        sqrt = int(min_num**0.5)
        min_nums = []

        for i in range(2, sqrt + 1):
            if min_num % i == 0:
                min_nums.append(i)
        for x in min_nums.copy():
            min_nums.append(min_num // x)
        min_nums.append(min_num)
        j = False
        res = []
        # print(min_nums)
        for min_num in min_nums:
            for v in dic.values():
                if v % min_num == 0:
                    pass
                else:
                    j = False
                    res.append(j)
                    break
            else:
                j = True
                res.append(j)
        return max(res)


deck = [1, 2, 3, 4, 4, 3, 2, 1]
s = Solution()
print(s.hasGroupsSizeX(deck))
# s.test(deck)
