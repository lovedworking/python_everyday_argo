class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 如果为负数 或者末位为0但不是0的数字也不能是回文数
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        # 当x还大于回文数继续反转
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x = x // 10
        return x == reversed_num or x == reversed_num // 10


sol = Solution()
print(sol.isPalindrome(121))