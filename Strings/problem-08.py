# 8. String to Integer (atoi)
class Solution:
    def myAtoi1(self, str: str) -> int:
        # pattern = re.compile('[0-9+-]')
        idx = 0
        digit = 0
        sign = 1
        signFlag = False
        digitFlag = False
        while (idx < len(str)):            
            if str[idx].isdigit():
                digit = (digit*10) + int(str[idx])
                signFlag = True
                digitFlag = True
            elif not digitFlag and (str[idx]==' '):
                idx += 1
                continue
            elif not signFlag and (str[idx]=='+' or str[idx]=='-'):
                sign = 1 if str[idx]=='+' else -1
                signFlag = True
                digitFlag = True
            else:
                break

            idx += 1
        if sign > 0 and digit > ((2**31)-1):
            digit = (2**31)-1
        elif sign < 0 and digit > (2**31):
            digit = 2**31
        
        if digit:
            return int(sign) * digit
        else:
            return 0

    def myAtoi(self, str):
        import re
        str = str.strip()
        str = re.findall('(^[\+\-0]*\d+)\D*', str)
        print(str)
        try:
            result = int(''.join(str))
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if result > MAX_INT > 0:
                return MAX_INT
            elif result < MIN_INT < 0:
                return MIN_INT
            else:
                return result
        except:
            return 0

# Test
solution = Solution()
# Expected: 0
print(solution.myAtoi("-   234"))
# Expected: 0
print(solution.myAtoi("   +0 123"))
# Expected: 42
print(solution.myAtoi("42"))
# Expected: -42
print(solution.myAtoi("  -42"))
# Expected: 4193
print(solution.myAtoi("4193 with words"))
# Expected: 0
print(solution.myAtoi("words and 987"))
# Expected: -2147483648
print(solution.myAtoi("-91283472332"))
# Expected: 0
print(solution.myAtoi("--1"))