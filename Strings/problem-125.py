# 125. Valid Palindrome
class Solution:
    def isPalindrome1(self, s):
        import re
        s = re.sub(r'\W+', '', s).lower()
        return s == s[::-1]
    
    def isPalindrome2(self, s):
        import re
        pattern = re.compile("[^a-zA-Z0-9]+")
        s = pattern.sub('', s).lower()
        return s == s[::-1]

    def isPalindrome(self, s):
        l = 0
        r = len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True


# Test
solution = Solution()
# Expected: True
print(solution.isPalindrome("A man, a plan, a canal: Panama"))