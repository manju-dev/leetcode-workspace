# 242. Valid Anagram
import collections
class Solution:
    def isAnagram1(self, s, t):
        if len(s) != len(t):
            return False
        sDict = {}
        tDict = {}
        for idx in range(len(s)):
            sDict[s[idx]] = sDict.get(s[idx], 0) + 1
            tDict[t[idx]] = tDict.get(t[idx], 0) + 1
        return sDict == tDict

    def isAnagram2(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram3(self, s, t):
        return sorted(s) == sorted(t)

    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        charCounter = {}
        for idx in range(len(s)):
            charCounter[s[idx]] = charCounter.get(s[idx], 0) + 1
            charCounter[t[idx]] = charCounter.get(t[idx], 0) - 1
        for val in charCounter.values():
            if val != 0:
                return False
        return True

# Test
solution = Solution()
# Expected: True
print(solution.isAnagram("anagram", "nagaram"))