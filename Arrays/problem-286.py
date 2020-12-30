# 283. Move Zeroes
class Solution:
    # Approach 1
    def moveZeroes1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < (len(nums)-(1+j)):
            if nums[i] == 0:
                nums[i:] = nums[i+1:]
                nums.append(0)
                j += 1
            else:
                i += 1
                
    # Approach 2
    def moveZeroes2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        while i < (len(nums)-(1+j)):
            if nums[i] == 0:
                del(nums[i])
                nums.append(0)
                j += 1
            else:
                i += 1
    
    # Approach 3 - Space Optimal, Operation Sub-Optima
    def moveZeroes3(self, nums) -> None:
        i = 0
        for index in range(len(nums)):
            if nums[index] != 0:
                nums[i] = nums[index]
                i += 1
        
        nums[i:] = [0] * (len(nums)-i)

    # Approach 3 - Optimal
    def moveZeroes(self, nums) -> None:
        foo = 0
        for bar in range(len(nums)):
            if nums[bar] != 0:
                nums[foo], nums[bar] = nums[bar], nums[foo]
                foo += 1

# Test
solution = Solution()
# Expected: [1, 16, 2, 0, 0]
nums = [1, 16, 0 , 2, 0]
solution.moveZeroes(nums)
print(nums)