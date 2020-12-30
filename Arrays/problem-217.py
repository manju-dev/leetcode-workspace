# Problem 217: Contains Duplicate
class Solution:
    # Approach 1 - Using sort
    def containsDuplicate(self, nums) -> bool:
        nums.sort()
        for index in range(len(nums)-1):
            if nums[index] == nums[index+1]:
                return True
        return False
    
    # Approach 2 - Using built-in count method
    def containsDuplicate2(self, nums) -> bool:
        for num in nums:
            if nums.count(num) > 1:
                return True
        return False
    
    # Approach 3 - Using visited list
    def containsDuplicate3(self, nums) -> bool:
        foo = []
        for num in nums:
            if num in foo:
                return True
            else:
                foo.append(num)
        return False

    # Approach 4 - Using Set
    def containsDuplicate4(self, nums: List[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False

# Test
solution = Solution()
# Expected: True
nums = [1,2,3,4,5,6,1]
print(solution.containsDuplicate(nums))