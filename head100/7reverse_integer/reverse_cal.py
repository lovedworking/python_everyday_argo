"""

整数除法 // 会向下取整   负数取 // +1
>>> -234 // 10
-24
>>> -234%10
6
>>> -234%10 - 10
-4
>>> (-234 - (-4)) // 10
-23

"""
class Solution:
    def reverse(self, x: int) -> int:
        MIN, MAX = -2**31, 2**31 - 1
        rev = 0
        while x != 0:
            # MIN是负数 不能写 rev < MIN // 10
            if rev < MIN // 10 + 1 or rev > MAX // 10:
                return 0
            # 弹出一位
            digit = x % 10
            # python3 取模运算 x为负 会返回【0,9)结果
            if x < 0 and digit > 0 :
                digit -= 10

            # python3 整数处理在x为负数 会向下 取整 不能写成 x //= 10
            x = (x-digit) // 10
            rev = rev*10 + digit

        return rev



sol = Solution()
print(sol.reverse(-123))