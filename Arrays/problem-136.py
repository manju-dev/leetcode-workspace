# Problem 136: Single Number
class Solution:
    # Approach 1 - Sort
    def singleNumber1(self, nums) -> int:
        if nums == []:
            return None
        
        nums.sort()
        index = 0
        while index != len(nums)-1 and nums[index] == nums[index+1]:
            index += 2
        return nums[index]

    # Approach 2 - Arithmetic
    def singleNumber(self, nums) -> int:
        return (2 * sum(set(nums))) - sum(nums)

    # Approach 3 - Bit manipulation - XOR
    def singleNumber3(self, nums) -> int:
        foo = 0
        for num in nums:
            foo = foo ^ num
        return foo

# Test
solution = Solution()
# Expected: 1
nums = [2,3,2,3,6,1,6]
print(solution.singleNumber(nums))
