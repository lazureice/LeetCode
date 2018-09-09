'''我的做法比较朴素，先找到大于等于N的第一个palindrome，检查是否是质数，如果不是则找到大于这个palindrome的下一个palindrome

找到大于等于某个n的palindrome方法如下：

对于低位（对称的右半部分），如果该位值大于对称位的值，则向前进位，该位置为0
把低位置为和对称位相等的值
注意下边界情况比如N=1时应该返回2'''


class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True

        # 欣宜用的递归，我觉得不需要啊
        def mypalind(n):
            x = str(n)
            length = len(x)
            for i in range(int(length / 2)):  # [-1]:
                if x[-1 - i] > x[i]:
                    n = n + (10 - int(x[-1 - i])) * (10**i)
                    x = str(n)
            x = list(x)
            for i in range(int(length / 2)):
                x[-1 - i] = x[i]
            return int(''.join(x))

        if N == 1:
            return 2

        t = mypalind(N)

        while not is_prime(t):
            t = mypalind(t + 1)

        return t

# ------------------

s = Solution()
ans = s.primePalindrome(101100)

print('result:', ans)

# --------------------
# 费马定理


def check(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    if pow(2, n - 1, n) != 1:
        return False
    return True


print(check(101101))
print(check(129921))
print(check(1837381))

# 有一个soln是用费马定理来检测的，但是有三个合数无法判断。不知道他是怎么AC的。
