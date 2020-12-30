# 387. First Unique Character in a String
class Solution:
    def firstUniqChar1(self, s):
        charCounts = {}
        for char in s:
            charCounts[char] = charCounts.get(char, 0) + 1
        for key, val in charCounts.items():
            if val == 1:
                for i in range(len(s)):
                    if key == s[i]:
                        return i
        return -1

    def firstUniqChar2(self, s):
        charCounts = {}
        for char in s:
            charCounts[char] = charCounts.get(char, 0) + 1
        for key, val in charCounts.items():
            if val == 1:
                return s.find(key)
        return -1

    def firstUniqChar(self, s):
        # build hash map : character and how often it appears
        import collections
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

# Test
solution = Solution()
# Expected: 2
print(solution.firstUniqChar("loveleetcode"))
# Expected: -1
print(solution.firstUniqChar("cc"))
# Expected: 0
print(solution.firstUniqChar("z"))
# Expected: -1
print(solution.firstUniqChar("aadadaad"))