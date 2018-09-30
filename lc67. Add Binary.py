class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ''
        mask = 0
        for i in range(1, 2 + max(len(a), len(b))):
            if len(a) >= i:
                tem_a = int(a[-i])
            else:
                tem_a = 0
            if len(b) >= i:
                tem_b = int(b[-i])
            else:
                tem_b = 0
            num = mask + tem_a + tem_b
            q = num // 2
            r = num % 2
            res = str(r) + res
            mask = q
        if res[0] == '0':
            res = res[1:]
        return res


a = "1010"
b = "1011"
s = Solution()
print(s.addBinary(a, b))

# 也可以直接调用内置函数
# return str(bin(int(a, 2) + int(b, 2)))[2:]
# int(a,2) 以2进制表示的str，转为int
# bin(n) 转为二进制 如：'0b1011'
# 所以最后才去掉前两位
