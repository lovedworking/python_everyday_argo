class Solution(object):
    """
    dividend = (quotient) * divisor + remainder
    """

    def divide(self, dividend, divisor):
        # 处理除零错误
        if divisor == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        # 处理溢出情况
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # 确定商的符号
        #  - ^ - = +, + ^ - = -, - ^ + = -
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # 将被除数和除数转换为正数
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0
        while dividend >= divisor:
            # 找到可以从被除数中减去的最大除数的倍数
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            # 从被除数中减去除数的倍数
            dividend -= temp
            quotient += multiple

        return sign * quotient

sol = Solution()
print(sol.divide(-20, 3))