"""
和12的区别在哪里 两个相反的操作
从右向左代表小数到大数
1 如果左边数字代表的值比右边小时 代表要执行减法
2 如果左边比右边大或者相等时  就执行加法
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN_DIC = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        prev = 0
        for letter in s[::-1]:
            value = ROMAN_DIC[letter]
            if value >= prev:
                res += value
            else:
                res -= value
            prev = value

        return res

sol = Solution()
print(sol.romanToInt('III'))

