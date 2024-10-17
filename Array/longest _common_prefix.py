from typing import List 


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_length = min(strs, key= len)

        for i, char  in enumerate(min_length):
            for str in strs:
                if str[i] != char:
                    return min_length[:i]

        return min_length

solution = Solution()
strs = ["ab", "a"]
result = solution.longestCommonPrefix(strs)
print(result)