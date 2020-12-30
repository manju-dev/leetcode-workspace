# Problem 26: Remove Duplicates from Sorted Array
class Solution:
    # Approach 1
    def removeDuplicates(self, nums) -> int:
        '''
        input:
        nums - list of integers
        returns: an int, length of the first unique values in array
        '''
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
    # Approach 2
    def removeDuplicates2(self, nums) -> int:
        newTail = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[newTail]:
                newTail += 1
                nums[newTail] = nums[i]
                
        return newTail + 1

# Test
solution = Solution()
# length = 2, with the first elements of nums being 1 and 2
nums = [1,1,2]
print(solution.removeDuplicates(nums))
print(nums)
# 5, with the first elements of nums being 0, 1, 2, 3, and 4
nums = [0,0,1,1,1,2,2,3,3,4]
print(solution.removeDuplicates(nums))
print(nums)