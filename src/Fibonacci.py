import time
class Solution:

    pre = 0
    """ 存储fibonacci(n)的值 """
    post = 0
    """ 存储fibonacci(n - 1)的值 """

    @classmethod
    def fibonacci(cls, n):

        """
        核心算法原理：
        观察: a(n)  = a(n - 1) + a(n - 2)
                   = 2 * a(n - 2) + a  (n - 3)
                   = 3 * a(n - 3) + 2 * a(n - 4)
                   = 5 * a(n - 4) + 3 * a(n - 5)
                   = ... ...
                   = a(k)  *  a(n - k + 1) + a(k - 1) * a(n - k)
        1、若令 n = 2k
            得 a(2k) = a(k)  * a(k + 1) + a(k-1) * a(k)
                    = a(k) * [a(k) + a(k - 1)] + a(k-1) * a(k)
                    = a(k) ^ 2 + 2 * a(k)  *  a(k - 1)
        2、若令 n = 2k - 1
            得 a(2k - 1) = a(k) * a(k) + a(k - 1)  * a(k - 1)
                    = a(k)  ^ 2 +  a(k - 1) ^ 2

        :param n: The location user want in fibonacci array
        :return: The fibonacci number in the special location
        """

        if n <= 2:
            # if   n = 0            #=> 0
            # else n = 1 || n = 2   #=> 1

            if n == 0:
                return 0
            cls.pre = 1
            cls.post = 1
            return cls.pre

        if n % 2 == 1:
            # n 为奇数， 则做减一操作， 函数回调时
            #        pre：        f(n) = f(n - 1) + f(n - 2)
            #        post：   f(n - 1) = f(n) - f(n - 2)
            cls.fibonacci(n - 1)
            cls.pre += cls.post
            cls.post = cls.pre - cls.post
            return cls.pre

        # 核心算法
        cls.fibonacci(n / 2)
        temp = cls.pre
        cls.pre = cls.pre * cls.pre + 2 * cls.pre * cls.post
        cls.post = temp * temp + cls.post * cls.post
        return cls.pre


n = 1000
solution = Solution()
print(solution.fibonacci(n))
print(time.process_time(), "seconds")