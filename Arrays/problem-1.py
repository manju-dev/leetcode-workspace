# 1. Two Sum
class Solution:
    # Approach 1 : Naive
    def twoSum1(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i, j]
        return None
    
    # Approach 2: Two-pass Hash Table
    def twoSum2(self, nums, target):
        foo = {}
        for i,j in enumerate(nums):
            foo[j] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in foo) and (foo.get(complement) != i):
                return [i, foo.get(complement)]
        return None
    
    # Approach 3: One-pass Hash Table
    def twoSum(self, nums, target):
        foo = {}
        for i,j in enumerate(nums):
            complement = target-j
            if (complement in foo):
                return [foo.get(complement), i]
            foo[j] = i
        return None

# Test
solution = Solution()
# Expected: []
nums = [1, 16, 0 , 2, 0]
print(solution.twoSum(nums, 18))