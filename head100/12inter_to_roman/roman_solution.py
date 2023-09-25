"""
每次尽量取最大面额的数字对应的罗马符号去解释
把对应面额对应全部列举出来然后计算差值 直到最后为0即可
"""
class Solution:
    NUMBER_PAIRS = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
    ]
    def intToRoman(self, num: int) -> str:
        res = list()
        for key, roman in Solution.NUMBER_PAIRS:
            while num >= key:
                num = num - key
                res.append(roman)
            if num == 0:
                break
        return "".join(res)

sol = Solution()
print(sol.intToRoman(1994))