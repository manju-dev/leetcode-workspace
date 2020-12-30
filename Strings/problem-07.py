# 7. Reverse Integer
class Solution:
    def reverse1(self, x):
        if (x == 0):
            return 0
        
        foo = ""
        flag = True if x < 0 else False
        x = abs(x)
        while abs(x) > 0:
            bar = x % 10
            x = x // 10
            foo += str(bar)
        
        if (int(foo) > 2**31):
            return 0
        else:
            return -(int(foo)) if flag else int(foo) 

    def reverse(self, x):
        foo = 0
        flag = True if x < 0 else False
        x = abs(x)
        while x > 0:
            bar = x % 10
            x = x // 10
            foo = foo * 10 + bar

            if (foo > 2**31):
                return 0

        return -(foo) if flag else foo 

# Test
solution = Solution()
# Expected: 321
print(solution.reverse(123))
# Expected: 21
print(solution.reverse(120))
# Expected: -123
print(solution.reverse(-321))
# Expected: 0
print(solution.reverse(1534236469))