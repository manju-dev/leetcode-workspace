# 38. Count and Say
class Solution:
    def countAndSay1(self, n):
        if n == 0:
            return ""
        output = "1"
        for _ in range(1, n):
            foo = ""
            idx = 0
            while idx < len(output):
                count = 1
                while (idx+1 < len(output)) and (output[idx]==output[idx+1]):
                    count += 1
                    idx += 1
                foo += str(count) + output[idx]
                idx += 1
            output = foo
        return output

    def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s

# Test
solution = Solution()
# Expected: 1211
print(solution.countAndSay(4))