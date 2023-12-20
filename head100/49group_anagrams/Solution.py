# <p>Given an array of strings <code>strs</code>, group <strong>the anagrams</strong> together. You can return the answer in <strong>any order</strong>.</p>
#
# <p>An <strong>Anagram</strong> is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.</p>
#
# <p>&nbsp;</p>
# <p><strong class="example">Example 1:</strong></p>
# <pre><strong>Input:</strong> strs = ["eat","tea","tan","ate","nat","bat"]
# <strong>Output:</strong> [["bat"],["nat","tan"],["ate","eat","tea"]]
# </pre>
# <p><strong class="example">Example 2:</strong></p>
# <pre><strong>Input:</strong> strs = [""]
# <strong>Output:</strong> [[""]]
# </pre>
# <p><strong class="example">Example 3:</strong></p>
# <pre><strong>Input:</strong> strs = ["a"]
# <strong>Output:</strong> [["a"]]
# </pre>
# <p>&nbsp;</p>
# <p><strong>Constraints:</strong></p>
#
# <ul>
#  <li><code>1 &lt;= strs.length &lt;= 10<sup>4</sup></code></li>
#  <li><code>0 &lt;= strs[i].length &lt;= 100</code></li>
#  <li><code>strs[i]</code> consists of lowercase English letters.</li>
# </ul>
#
# <div><div>Related Topics</div><div><li>数组</li><li>哈希表</li><li>字符串</li><li>排序</li></div></div><br><div><li>👍 1766</li><li>👎 0</li></div>

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) <= 1:
            return [strs]
        group_dict = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            group_dict.setdefault(sort_word, []).append(word)
        return list(group_dict.values())

# leetcode submit region end(Prohibit modification and deletion)

sol = Solution()
print(sol.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"]))
