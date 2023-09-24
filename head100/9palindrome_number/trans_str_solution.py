"""
转为字符串来解 就和最长回文子串解决方式一样了 但是这个是判断整体是不是
从两头开始判断就可以了

"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        lx = str(x)
        print(lx)
        for i in range(len(lx)//2):
            if lx[i] != lx[-(i + 1)]:
                return False
        return True


sol = Solution()
print(sol.isPalindrome(6312136))