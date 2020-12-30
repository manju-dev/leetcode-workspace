# 344. Reverse String
class Solution:
    def reverseString1(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[~i] = s[~i], s[i]

    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]

# Test
solution = Solution()
# Expected: ['o', 'l', 'l', 'e', 'h']
foo = ["h","e","l","l","o"]
solution.reverseString(foo)
print(foo)