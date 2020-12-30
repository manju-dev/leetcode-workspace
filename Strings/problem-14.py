# 14. Longest Common Prefix
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        output = ""
        idx = 0
        while idx < len(strs[0]):
            letter = strs[0][idx]
            for word in strs[1:]:
                if idx >= len(word) or word[idx]!=letter:
                    return output
            output += letter
            idx += 1
        return output

# Test
solution = Solution()
# Expected: "fl"
print(solution.longestCommonPrefix(["flower","flow","flight"]))
# Expected: "c"
print(solution.longestCommonPrefix(["c","c"]))