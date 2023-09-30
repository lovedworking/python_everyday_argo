class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return list()
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def back_track(index: int):
            if index == len(digits):
                res_lists.append("".join(sub_list))
            else:
                digit = digits[index]
                for letter in phone_map[digit]:
                    sub_list.append(letter)
                    back_track(index + 1)
                    sub_list.pop()

        sub_list = list()
        res_lists = list()
        back_track(0)
        return res_lists


sol = Solution()
print(sol.letterCombinations("23"))