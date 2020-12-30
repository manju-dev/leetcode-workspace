# 66. Plus One
class Solution:
    # Approach 1:
    def plusOne1(self, digits):
        foo = []
        idx = -1
        
        # if last digit can be incremented without overflow
        if digits[-1] < 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        # when the last digit overflows
        while (abs(idx) <= len(digits)) and (digits[idx] == 9):
            foo.append(0)
            idx -= 1
        foo.append(1)
        
        foo.reverse()
        if abs(idx+1) == len(digits):
            return foo
        else:
            digits[idx] += 1
            return digits[:idx+1] + foo[1:]
    
    # Approach 2:
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        return [1] + ([0] * (len(digits)))
    
    # Approach 3:
    def plusOne3(self, digits):
        foo = ''
        for i in digits:
            foo += str(i)
        return [int(i) for i in str(int(foo) + 1)]
    
    # Approach 4:
    def plusOne3(self, digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, (len(digits)-1-i))
        return [int(i) for i in str(num+1)]

# Test
solution = Solution()
# Expected: 1
digits = [5, 9, 9, 9]
print(solution.plusOne(digits))