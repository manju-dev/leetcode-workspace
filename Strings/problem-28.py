# 28. Implement strStr()
class Solution:
    def strStr(self, haystack, needle):
        for i in range(0, (len(haystack) - len(needle) + 1)):
            if haystack[i : (i + len(needle))] == needle:
                       return i
        return -1

# Test
solution = Solution()
# Expected: 2
print(solution.strStr("hello", "ll"))